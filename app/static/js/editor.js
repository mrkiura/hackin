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
    var urlHash = window.location.hash.replace(/#/g, '');
    if (urlHash) {
        fbRef = fbRef.child(urlHash);
    } else {
        fbRef = fbRef.push(); // generate unique location.
        window.location = window.location + '#' + fbRef.key(); // add it as a hash to the URL.
    }
    return fbRef;
}

window.onload = configEditor;
