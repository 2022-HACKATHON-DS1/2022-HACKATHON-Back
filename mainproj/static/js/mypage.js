const button1 = document.querySelector('.view-but');

button1.addEventListener('click', () => {
    const dropyear = document.querySelector('.dropyear');
    dropyear.classList.toggle('dis2');
});


//이미지 업로드 기능
function loadFile(input) {
    var file = input.files[0];	//선택된 파일 가져오기
  
    //새로운 이미지 div 추가
    var newImage = document.createElement("img");
    newImage.setAttribute("class", 'img');
  
    //이미지 source 가져오기
    newImage.src = URL.createObjectURL(file);   
  
    newImage.style.width = "100%";
    newImage.style.height = "100%";
    //newImage.style.objectFit = "fill";
  
    //이미지를 image-show div에 추가
    var container = document.getElementById('img');
    container.appendChild(newImage);
  };
  
