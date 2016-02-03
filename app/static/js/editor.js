// initialize data store and the editors
var startEditor = function() {
    var editor = ace.edit('firepad');
    editor.$blockScrolling = Infinity;
    editor.setTheme("ace/theme/monokai");
    editor.setFontSize(14)
    var session = editor.getSession();
    session.setUseWrapMode(true);
    session.setUseWorker(false);
    session.setMode("ace/mode/python");

    var firepad = Firepad.fromACE(getUserRef(), editor, {
        defaultText: '# Hack in python'
    });
}

var getUserRef = function() {
   var fbRef = new Firebase('https://hack-in.firebaseio.com');
      var hash = window.location.hash.replace(/#/g, '');
      console.log(hash)
      console.log(fbRef)
      if (hash) {
        fbRef = fbRref.child(hash);
      } else {
        fbRef = fbRef.push(); // generate unique location.
        window.location = window.location + '#' + fbRef.key(); // add it as a hash to the URL.
      }
      if (typeof console !== 'undefined')
        console.log('Firebase data: ', fbRef.toString());
      return fbRef;
}

window.onload = startEditor;
