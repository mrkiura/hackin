var rootRef = new Firebase('https://hack-in.firebaseio.com');
username = $('#username').text();
session_id = $('#session_id').text();
sessionsRef = 'https://hack-in.firebaseio.com/'

$(document).ready(function() {
    url_ = '';
    setTimeout(function() {
        url_ = window.location.pathname + window.location.hash;

        // send session details to server
        $.ajax({
            type: 'POST',
            url: '/fromajax',
            data: JSON.stringify({
                id_: session_id,
                username: username,
                session_url: url_
            }, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                console.log(result);
            }
        });

    }, 3000);


});

var configEditor = function() {
    // Get a firebase reference
    var firepadRef = getFirebaseRef();

    //// Create ACE
    var editor = ace.edit('firepad');
    editor.setTheme('ace/theme/monokai');
    editor.setFontSize(20)
    var session = editor.getSession();
    session.setUseWrapMode(true);
    session.setUseWorker(false);
    session.setMode('ace/mode/python');

    // start a firepad instance
    var firepad = Firepad.fromACE(firepadRef, editor, {
        defaultText: '# let\'s write some python'
    });
}

//get's a firebase ref, and adds a hash to the url
var getFirebaseRef = function() {
    var fbRef = new Firebase('https://hack-in.firebaseio.com');
    urlHash = window.location.hash.replace(/#/g, '');
    if (urlHash) {
        fbRef = fbRef.child(urlHash);
    } else {


        fbRef = fbRef.push(); // generate unique location.
        window.location = window.location + '#' + fbRef.key(); // add it as a hash to the URL.
    }
    setTimeout(saveUserSession, 5000)
    return fbRef;
}

var saveUserSession = function() {
    sessionInfo = {
        username: $('#username').text(),
        session: window.location.hash.replace(/#/g, '')
    }

    var rootRef = new Firebase('https://hack-in.firebaseio.com');
    childRef = $('#username').text();
    var sessionsRef = rootRef.child(childRef);
    pushOnline(sessionInfo, sessionsRef);
}

var pushOnline = function(object, ref) {
    var newRef = ref.push();
    newRef.set(object);
}
if (window.location.pathname.indexOf('new')) {
    window.onload = configEditor;
}
