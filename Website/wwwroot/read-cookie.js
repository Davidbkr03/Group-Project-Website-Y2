window.checkCookieExists = function (cookieName) {
    var allCookies = document.cookie.split(';');
    for (var i = 0; i < allCookies.length; i++) {
        var cookiePair = allCookies[i].trim();
        if (cookiePair.startsWith(cookieName + '=')) {
            return true;
        }
    }
    return false;
}
