var configEditor = function() {
    // Get a firebase reference
    var firepadRef = getFirebaseRef();

    //// Create ACE
    var editor = ace.edit("firepad");
    editor.setTheme("ace/theme/monokai");
    editor.setFontSize(20)
    var session = editor.getSession();
    session.setUseWrapMode(true);
    session.setUseWorker(false);
    session.setMode("ace/mode/python");

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
        if (window.location.pathname.indexOf('home')) {
            break;
        }
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
    console.log(sessionInfo);
    var rootRef = new Firebase('https://hack-in.firebaseio.com');
    childRef = $('#username').text();
    var sessionsRef = rootRef.child(childRef);
    pushOnline(sessionInfo, sessionsRef);
}

var pushOnline = function(object, ref) {
  var newRef = ref.push();
  newRef.set(object);
}

window.onload = configEditor;

// saveUserSession();
