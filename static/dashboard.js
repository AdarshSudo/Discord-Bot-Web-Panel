// ---------------DASHBOARD HTML------------------
  function logout() {
      // Clear the browser history
      window.history.replaceState({}, document.title, "/");
      window.location.href = "/logout";
  }
  
// ----------------------------------------