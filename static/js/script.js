async function send(){

    let input=document.getElementById("message");

    let msg=input.value;

    document.getElementById("messages").innerHTML+=
    "<p><b>You:</b> "+msg+"</p>";

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:msg
        })
    });

    const data=await response.json();

    document.getElementById("messages").innerHTML+=
    "<p><b>AI:</b> "+data.response+"</p>";

    input.value="";
}