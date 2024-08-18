
 var signup=document.getElementById("signupid");
 var support=document.getElementById("supportid");
 var services=document.getElementById("servicesid");
 var features=document.getElementById("Featuresid");
 var TalkHuman=document.getElementById("TalkHumanid");

 function funcf1(){
 signup.style.display="block";
 }
 function funcf2(){
 support.style.display="block";
 }
 function funcf3(){
  services.style.display="block";
 }
 function funcf4(){
 features.style.display="block";
 }
 function funcf5(){
 TalkHuman.style.display="block";
 }

function funcsubmit(){
swal("Recorded!", "Our Team will get back to you soon!", "success");
alert("Thanks, Your Details have been recorded, our team will contact you soon.");
}