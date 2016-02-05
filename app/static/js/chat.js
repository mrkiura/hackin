  var messagesRef = new Firebase('https://hack-in.firebaseio.com/chats');

 
  var messageField = $('#messageInput');
  var nameField = $('#nameInput');
  var messageList = $('#messages');

 
  messageField.keypress(function (e) {
    // on pressing enter
    if (e.keyCode == 13) {
  
      var username = nameField.val();
      var message = messageField.val();

 
      messagesRef.push({name:username, text:message});
      messageField.val('');
    }
  });


  messagesRef.limitToLast(12).on('child_added', function (snapshot) {

    var data = snapshot.val();
    var username = data.name || "anonymous";
    var message = data.text;

 
    var messageElement = $("<li>");
    var nameElement = $("<strong class='chat-username'></strong>")
    nameElement.text(username);
    messageElement.text(message).prepend(nameElement);

   
    messageList.append(messageElement)
// check 
   
    messageList[0].scrollTop = messageList[0].scrollHeight;
  });