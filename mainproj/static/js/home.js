//imgUrlList=['3.png','2.png','1.png','7.png','8.png'];

imgUrlList=[
    {imgSrc:'../img/3.png',
     imgIdx:0},

     {imgSrc:'../img/2.png',
     imgIdx:1},

     {imgSrc:'../img/1.png',
     imgIdx:2},

     {imgSrc:'../img/7.png',
     imgIdx:3},

     {imgSrc:'../img/8.png',
     imgIdx:4},
]

function showImg(){
    for (let i in imgUrlList){
        // 이미지 사이즈 구하기
        let img=new Image();
        let tapeimg=new Image();

        img.src=imgUrlList[i].imgSrc;
        tapeimg.src='../img/tape.png';

        let width=img.width;
        let height=img.height;
        let tapewidth=tapeimg.width;
        let tapeheight=tapeimg.height;

        // 이미지 랜덤 rotate값 , 홀 수번째 이미지일때 - 붙게        
        var randomRotate=Math.floor((Math.random()*(10-1)+1)+3);
        if(i%2){
          randomRotate= -1 * randomRotate;
        }
        //console.log(randomRotate);

        var contents=document.querySelector('.contentsDiv');
        var imgDiv=document.createElement('div');

        contents.appendChild(imgDiv);
        imgDiv.classList.add('imgDiv');

        var imgimg=document.createElement('img');
        var tape=document.createElement('img');
        tape.classList.add('imagetape');
        imgimg.classList.add('imgimg');

        tape.style.left= (width/3)+"px";
        tape.style.top= "-" + (height + (tapeheight/2)) + "px";

        imgimg.style.rotate= randomRotate + "deg";
        tape.style.rotate=-1 * randomRotate+ "deg";

        imgimg.src=imgUrlList[i].imgSrc;
        tape.src='../img/tape.png';

        imgDiv.appendChild(imgimg);
        imgDiv.appendChild(tape);

        imgimg.addEventListener('click',()=>{
            // imgUrlList[i].imgIdx 를 이용해서 세부 페이지 이동
            location.href="";
        })
        
    }
}


