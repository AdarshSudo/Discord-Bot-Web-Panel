
// ---------GUILD HTML ONLOAD-----------
window.onload = function() {
  // Simulating database values, replace with actual database retrieval
  var checkbox1 = document.getElementById("toggleSwitch");
  var checkbox2 = document.getElementById("checkbox2");
  var checkbox3 = document.getElementById("checkbox3");
  var checkbox4 = document.getElementById("checkbox4");
  var selectField = document.getElementById("selectOptionField");

  // Set the state of checkbox2 and checkbox3 based on toggleSwitch's state
  checkbox2.disabled = !checkbox1.checked;
  checkbox3.disabled = !checkbox1.checked;
  checkbox4.disabled = !checkbox1.checked;

  if (checkbox4.checked) {
    selectField.classList.remove("hidden"); // Show select option field
    console.log("done")
  } else {
    selectField.classList.add("hidden"); // Hide select option field
    console.log("not done")
  }

}

// ----------------------------------------------



// ---------------GUILD HTML------------------

  function showSettings() {
    // Hide the welcome and goodbye container
    document.getElementById('welcomeGoodbye').style.display = 'none';
    // Show the settings page container
    document.getElementById('settingsPage').style.display = 'block';
  }

  function goBack() {
    // Hide the settings page container
    document.getElementById('settingsPage').style.display = 'none';
    // Show the welcome and goodbye container
    document.getElementById('welcomeGoodbye').style.display = 'block';
  }

  function toggleCheckboxes() {
    var checkbox1 = document.getElementById("toggleSwitch");
    var checkbox2 = document.getElementById("checkbox2");
    var checkbox3 = document.getElementById("checkbox3");
    var checkbox4 = document.getElementById("checkbox4");
    var selectField = document.getElementById("selectOptionField");
  
    checkbox2.disabled = !checkbox1.checked;
    checkbox3.disabled = !checkbox1.checked;
    checkbox4.disabled = !checkbox1.checked;

    if (checkbox4.checked) {
      selectField.classList.remove("hidden"); // Show select option field
      console.log("done")
    } else {
      selectField.classList.add("hidden"); // Hide select option field
      console.log("not done")
    }

  }

  function toggleSwitch() {
    // Handle the toggle switch functionality here
    var switchState = document.getElementById("toggleSwitch").checked;
    var guildId = document.getElementById('guildId').value;
    // You can perform actions based on the switch state
    console.log('Switch state:', switchState ? 'ON' : 'OFF');
    var switch2 = document.getElementById("checkbox2");
    var switch3= document.getElementById("checkbox3");
    var switch4= document.getElementById("checkbox4");
    if (switch2.checked || switch3.checked || switch4.checked) {
      var temp_switchState2 = document.getElementById("checkbox2").checked = false;
      var temp_switchState3 = document.getElementById("checkbox3").checked = false;
      var temp_switchState4 = document.getElementById("checkbox4").checked = false;
      fetch('/toggle2', {
        method: 'POST',
        body: new URLSearchParams({ switch_state: temp_switchState2, guild_id: guildId }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })
      fetch('/toggle3', {
        method: 'POST',
        body: new URLSearchParams({ switch_state: temp_switchState3, guild_id: guildId }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })
      fetch('/toggle4', {
        method: 'POST',
        body: new URLSearchParams({ switch_state: temp_switchState4, guild_id: guildId }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })
    }
    // Send a POST request to Flask route to update the setting in the database
    fetch('/toggle', {
      method: 'POST',
      body: new URLSearchParams({ switch_state: switchState, guild_id: guildId }),
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return response.text();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));

}

function toggleSwitch2() {
  // Handle the toggle switch functionality here
  var switchState = document.getElementById("checkbox2").checked;
  var guildId = document.getElementById('guildId').value;
  // You can perform actions based on the switch state
  console.log('Switch state:', switchState ? 'ON' : 'OFF');
  // Send a POST request to Flask route to update the setting in the database
  fetch('/toggle2', {
    method: 'POST',
    body: new URLSearchParams({ switch_state: switchState, guild_id: guildId }),
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })
  .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.text();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));

}

function toggleSwitch3() {
  // Handle the toggle switch functionality here
  var switchState = document.getElementById("checkbox3").checked;
  var guildId = document.getElementById('guildId').value;
  // You can perform actions based on the switch state
  console.log('Switch state:', switchState ? 'ON' : 'OFF');
  // Send a POST request to Flask route to update the setting in the database
  fetch('/toggle3', {
    method: 'POST',
    body: new URLSearchParams({ switch_state: switchState, guild_id: guildId }),
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.text();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));
  
}

function toggleSwitch4() {
  // Handle the toggle switch functionality here
  var switchState = document.getElementById("checkbox4").checked;
  var guildId = document.getElementById('guildId').value;
  var checkbox = document.getElementById("checkbox4");
  var selectField = document.getElementById("selectOptionField");
  // You can perform actions based on the switch state
  console.log('Switch state:', switchState ? 'ON' : 'OFF');

  if (checkbox.checked) {
    selectField.classList.remove("hidden"); // Show select option field
    console.log("done")
  } else {
    selectField.classList.add("hidden"); // Hide select option field
    console.log("not done")
  }

  // Send a POST request to Flask route to update the setting in the database
  fetch('/toggle4', {
    method: 'POST',
    body: new URLSearchParams({ switch_state: switchState, guild_id: guildId }),
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })
  .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.text();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));
  
}


const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    appendAlert('Role and Channel ID updated succesfully!', 'primary')
  })
}



