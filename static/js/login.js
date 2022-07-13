document.getElementById("publisher").onsubmit = function(e){
    e.preventDefault();
    fetch('/publisher', {
        method : 'POST',
        body: JSON.stringify({
            'id': document.getElementById('id').value,
            'message': document.getElementById('message').value,
            'topic': document.getElementById('topic').value,
            'status': document.getElementById('status').value
        }),
        headers : {
            'Content-Type' : 'application/json'
        },
    }).then(function(response){
        return response.json()
    }).then(function(jsonResponse){
        console.log(jsonResponse)
        if(jsonResponse['error'] === false){
            alert("no se registro nada")`
            document.getElementById("error").className='hidden'
        }else{
            document.getElementById("error").className=''
            document.getElementById("error").innerHTML = jsonResponse['error_message']
        }
    }).catch(function(error) {
        console.log(error)
        document.getElementById("error").className=''
    });
    fetch('/subscriber', {
        method : 'GET',
        body: JSON.stringify({
            'id': document.getElementById('id').value,
            'message_view': document.getElementById('message_view').value,
            'topic_view': document.getElementById('topic_view').value,
            
        }),
        headers : {
            'Content-Type' : 'application/json'
},
}