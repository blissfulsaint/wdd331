function toggleNav() {
    var updateElement = document.getElementById("menu-icon");
    var updateNav = document.getElementById('nav-container');
    //toggle adds a class if it's not there or removes it if it is.
    updateElement.classList.toggle("open");
    updateNav.classList.toggle('open');
}

