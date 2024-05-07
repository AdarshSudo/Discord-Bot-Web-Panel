import discord
from discord.ext import commands
from flask import Flask, render_template, request, redirect, session, url_for , Response
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import pymongo
from pymongo.mongo_client import MongoClient
import json
from multiprocessing import Process
import os
import config 
from utils import get_token, get_user_name, get_user_guilds , get_bot_guilds, get_mutual_guilds, get_guild_data


bot = commands.Bot('+', intents=discord.Intents().all())

global user, mutualguild_collection
user = ' '
mutualguild_collection = None

#--------------------------------------------------MONGO DB SETUP--------------------------------------------------------------

uri = "mongodb+srv://Adarsh:hjmvgcNzc3BzUBOU@cluster0.oakdq2w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! PY")
except Exception as e:
    print(e)

db = client['discord_database']

guild_collection = db["guilds"]

# collection_name = dbname["user_1_items"]

# item_1 = {
#   "_id" : "U1IT00001",
#   "item_name" : "Blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340,
#   "category" : "kitchen appliance"
# }

# item_2 = {
#   "_id" : "U1IT00002",
#   "item_name" : "Egg",
#   "category" : "food",
#   "quantity" : 12,
#   "price" : 36,
#   "item_description" : "brown country eggs"
# }
# collection_name.insert_many([item_1,item_2])

#---------------------------------------------------------------------------------------------------------------------



app = Flask(__name__)
app.config['SECRET_KEY'] = "this_is_a_secret"


@bot.event
async def on_ready():
    print('bot ready to go')
    # Create a unique index on the 'id' and 'name' fields
    guild_collection.create_index([('id', pymongo.ASCENDING), ('name', pymongo.ASCENDING)], unique=True)
    for guild in bot.guilds:
        id = str(guild.id)
        name = guild.name
        try:
            guild_collection.insert_one({'id': id, 'name': name})

        except pymongo.errors.DuplicateKeyError:
            # Handle the case when there is a conflict (e.g., duplicate ID)
            print(f"Guild with ID {id} already exists in the collection.")
        
        print(
            f'{guild.name} (id: {guild.id})'
        )
    


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


@app.route('/callback')
def callback():
    token = get_token(request.args.get('code'))
    session['token'] = token
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'token' not in session:
        return redirect("https://discord.com/api/oauth2/authorize?client_id=894889958647693343&response_type=code&redirect_uri=http%3A%2F%2Fconnect2grp.live%2Fcallback&scope=identify+guilds")
    user_name = get_user_name(session.get('token'))
    user = user_name['username']
    mutualguild_collection = db[user]
    user_guilds = get_user_guilds(session.get('token'))
    bot_guilds = get_bot_guilds()
    mutual_guilds = get_mutual_guilds(user_guilds, bot_guilds)
    # Create a unique index on the 'id' and 'name' fields
    mutualguild_collection.create_index([('id', pymongo.ASCENDING), ('name', pymongo.ASCENDING)], unique=True)
    guild_collection.create_index([('id', pymongo.ASCENDING), ('name', pymongo.ASCENDING)], unique=True)
    for guild in mutual_guilds:
        id = guild['id']
        name = guild['name']
        main_welcome = False
        welcome_default = False
        goodbye_default = False
        role_giving = False
        default_img = None
        channel = None
        role = None
        try:
            mutualguild_collection.insert_one({'id': id, 'name': name})
            guild_collection.update_one({"id": id}, {"$set": {"main_welcome": main_welcome, "welcome_default":welcome_default , "goodbye_default": goodbye_default, "role_giving": role_giving, "default_img": default_img, "channel_id": channel, "role_name": role}}, upsert=True)
        except pymongo.errors.DuplicateKeyError:
            # Handle duplicates if needed
            print(f"Guild with ID {id} already exists in the collection.")
    
    return render_template('dashboard.html', guilds=mutual_guilds)

    

@app.route('/guild/<guild_id>')
def guild(guild_id: int):
    guild_info = get_guild_data(guild_id)
    if not guild_info:
        return redirect('/dashboard')
    setting_1 = guild_collection.find_one({"id": guild_id})
    setting_2 = guild_collection.find_one({"id": guild_id})
    setting_3 = guild_collection.find_one({"id": guild_id})
    setting_4 = guild_collection.find_one({"id": guild_id})
    return render_template('guild.html', guild=guild_info, setting1=setting_1['main_welcome'] if setting_1 else False, setting2=setting_2['welcome_default'] if setting_2 else False, setting3=setting_3['goodbye_default'] if setting_3 else False, setting4=setting_4['role_giving'] if setting_4 else False)


# Route to handle switch toggle
@app.route('/toggle', methods=['POST'])
def toggle():
    # Retrieve switch state from the HTML form
    switch_state = request.form['switch_state']
    guild_id = request.form['guild_id']
    switch_state = switch_state.lower() == 'true'
    # Update the setting value in the database
    guild_collection.update_one({"id": guild_id}, {"$set": {"main_welcome": switch_state}}, upsert=True)
    return 'Switch state updated successfully'

@app.route('/toggle2', methods=['POST'])
def toggle2():
    # Retrieve switch state from the HTML form
    switch_state = request.form['switch_state']
    guild_id = request.form['guild_id']
    switch_state = switch_state.lower() == 'true'
    # Update the setting value in the database
    guild_collection.update_one({"id": guild_id}, {"$set": {"welcome_default": switch_state}}, upsert=True)
    return 'Switch state updated successfully'

@app.route('/toggle3', methods=['POST'])
def toggle3():
    # Retrieve switch state from the HTML form
    switch_state = request.form['switch_state']
    guild_id = request.form['guild_id']
    switch_state = switch_state.lower() == 'true'
    # Update the setting value in the database
    guild_collection.update_one({"id": guild_id}, {"$set": {"goodbye_default": switch_state}}, upsert=True)
    return 'Switch state updated successfully'

@app.route('/toggle4', methods=['POST'])
def toggle4():
    # Retrieve switch state from the HTML form
    switch_state = request.form['switch_state']
    guild_id = request.form['guild_id']
    switch_state = switch_state.lower() == 'true'
    # Update the setting value in the database
    guild_collection.update_one({"id": guild_id}, {"$set": {"role_giving": switch_state}}, upsert=True)
    return 'Switch state updated successfully'

@app.route('/submit', methods=['POST'])
def submit():
    selected_option = request.form['selectedOption']  # Get the selected option from form data
    dc_id = request.form['channelid']
    guild_id = request.form['guild_id']
    # Update MongoDB collection with selected option
    guild_collection.update_one({"id": guild_id}, {"$set": {"role_name": selected_option}}, upsert=True)
    guild_collection.update_one({"id": guild_id}, {"$set": {"channel_id": dc_id}}, upsert=True)
    # return 'Role Updated successfully!'
    return Response(status=204)
    


#main------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def run_flask():
    app.run(host="0.0.0.0")
    
def run_discord():
    bot.run(config.token)
    
if __name__ == '__main__':
    flask_process = Process(target=run_flask)
    discord_process = Process(target=run_discord)
    flask_process.start()
    discord_process.start()
    flask_process.join()
    discord_process.join()

client.close()