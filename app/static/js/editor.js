// initialize data store and the editors

var firepadRef = new Firebase('https://hack-in.firebaseio.com');
var editor = ace.edit('firepad');
var firepad = Firepad.fromACE(firepadRef, editor);
