(function ($) {
    setTimeout(function(){
        uidFile = "MFRC522-python/uid.txt"; 
        jQuery.get(uidFile, function(data) {
            auth=document.getElementsByClassName("auth");
            p = document.querySelectorAll("div.auth p")
            if(data!=""){
                auth[0].style.backgroundColor = "#00c652";
                p[0].innerHTML="Autorise"
            }else{
                auth[0].style.backgroundColor = "#d50000";
                p[0].innerHTML="Refuse"
            }
            console.log("Suppression du fichier :");
            unlink(uidFile);
            console.log(data)
         });
    }, 500);
})(jQuery);