$(function(){

    let s_count = 1; //전역변수 (학생번호)
    let o_id = 0;
    let o_no = 0;
    let o_name = "";
    let o_kor = 0;
    let o_eng = 0;
    let o_math = 0;
    
    // let no = [1,2,3,4,5,6,7,8,9,10];
    // let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    // let kor = [62,90,64,76,51,89,77,55,73,53];
    // let eng = [70,62,73,54,55,60,67,77,51,100];
    // let math = [81,79,50,83,72,79,82,86,50,94];
    // let total = [213,231,187,213,178,228,226,218,174,247];
    // let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];
    $.ajax({
        url:"http://127.0.0.1:5500/z03_javascript_class/js0417/json/stu_score.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            alert('성공')
            s_count = data.length;
            let htmlData = "";
            for (let i=0;i<data.length;i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>0</td>";
                htmlData += "<td><button class='delBtn'>삭제</button></td>";
                htmlData += "</tr>";
            }//for
            $("#body").html(htmlData);
        },
        error:function(data){
            alert('실패')
        }
    })


    // tbody부분 10개 행 생성
    // html소스를 tbody 추가
    
    //검색
    $("#searchBtn").click(function(){
        console.log($("#s_word").val());
        if($("#s_word").val().length<1){
            alert('검색할 학생의 이름을 입력하세요')
            return false;
        }
        //alert("test");
        let s_word = $("#s_word").val()
        let htmlData = "";
        $.ajax({
            url:"http://127.0.0.1:5500/js0417/json/stu_score.json",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                //alert('성공')
                s_count = data.length;
                let htmlData = "";
                for (let i=0;i<data.length;i++){
                    if(data[i].name.indexOf(s_word) != -1){

                        htmlData += "<tr id='"+data[i].no+"'>";
                        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                        htmlData += "<td>"+data[i].no+"</td>";
                        htmlData += "<td>"+data[i].name+"</td>";
                        htmlData += "<td>"+data[i].kor+"</td>";
                        htmlData += "<td>"+data[i].eng+"</td>";
                        htmlData += "<td>"+data[i].math+"</td>";
                        htmlData += "<td>"+data[i].total+"</td>";
                        htmlData += "<td>"+data[i].avg+"</td>";
                        htmlData += "<td>0</td>";
                        htmlData += "<td><button class='delBtn'>삭제</button></td>";
                        htmlData += "</tr>";
                    }
                }//for
                $("#body").html(htmlData); 
            },
            error:function(data){
                alert('실패')
            }
        })
   
    });







    //학생입력확인 버튼
    $("#writeBtn").click(function(){
        if($(".stuChk:checked").length>=1){
            alert('학생입력을 하시려면 체크를 해제하셔야 합니다. \n자동으로 체크를 해제합니다.')
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
            return false;}
    
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop('readonly',false);
    });
    
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        $('#id').val("");
        $('#name').val("");
        $('#kor').val("");
        $('#eng').val("");
        $('#math').val("");

    });

    $("#confirmBtn").click(function(){      //입력, 수정 화면 공유중
        if($("#id").val()==""){

            // 글자-text() innerText, input-val() value, html() innerHtml
            //console.log(Math.max.apply(null,no)+1); //배열에서 최대값 구하기
            //no.push(Math.max.apply(null,no)+1); //배열추가
            
            console.log("이름 : "+$("#name").val());
            //let i_no = Math.max.apply(null,no)+1;
            let i_no = s_count+1;
            let i_name = $("#name").val();
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(2); //소수점2자리 반올림
            //table tr추가
            let htmlData = "";
            htmlData += "<tr id='"+i_no+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
            htmlData += "<td>"+i_no+"</td>";
            htmlData += "<td>"+i_name+"</td>";
            htmlData += "<td>"+i_kor+"</td>";
            htmlData += "<td>"+i_eng+"</td>";
            htmlData += "<td>"+i_math+"</td>";
            htmlData += "<td>"+i_total+"</td>";
            htmlData += "<td>"+i_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";
            // html소스를 tbody 추가
            $("#body").append(htmlData);
            $(".p_all").css("display","none");
        } //입력일 때 <확인>버튼 활성화 (id를 안 넣었음. 수정에선 hidden으로 넣었음.)

        else{
            //alert('수정을 완료합니다');

            o_no= $('#id').val();
            o_name = $('#name').val();
            o_kor = Number($('#kor').val());
            o_eng = Number($('#eng').val());
            o_math = Number($('#math').val());
            let o_total = o_kor+o_eng+o_math;
            let o_avg = o_total/3

            console.log("id: "+o_no);
            console.log("kor: "+o_kor);
            console.log("eng: "+o_eng);
            console.log("math: "+o_math);

            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += "<td>"+o_no+"</td>";
            htmlData += "<td>"+o_name+"</td>";
            htmlData += "<td>"+o_kor+"</td>";
            htmlData += "<td>"+o_eng+"</td>";
            htmlData += "<td>"+o_math+"</td>";
            htmlData += "<td>"+o_total+"</td>";
            htmlData += "<td>"+o_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            // html소스를 tbody 추가
            $("#"+o_no).html(htmlData);

            $(".p_all").css("display","none");

        }



    });//학생입력,수정 확인버튼
    


    $("#modifyBtn").click(function(){           //수정 버튼
        if($(".stuChk:checked").length!=1){
            alert('학생 1명만 선택하셔야 수정이 가능합니다.')
            return false;
        }
        o_id = $(".stuChk:checked").parent();
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text()
        o_eng = o_id.next().next().next().next().text()
        o_math= o_id.next().next().next().next().next().text()

        console.log('학번 :',o_id.next().text());
        console.log('이름 :',o_id.next().next().text());
        console.log('국어 :',o_id.next().next().next().text());
        console.log('영어 :',o_id.next().next().next().next().text());
        console.log('수학 :',o_id.next().next().next().next().next().text());

        $(".p_all").css("display","block");

        $(".p_main h2").text("학생성적수정");

        $('#id').val(o_no);
        $('#name').val(o_name);
        $('#kor').val(o_kor);
        $('#eng').val(o_eng);
        $('#math').val(o_math);  // 수정창 안에 

        
        
    });// modifyBtn (수정)




    //전체선택,취소
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        }
    });
    //table에 있는 삭제버튼 클릭
    $(".delBtn").click(function(){
        console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });//table삭제
    //하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        //alert("test");
        console.log("체크박스 개수 : "+$(".stuChk").length);
        console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
        console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);
        //체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.");
            return false;
        }//체크if
        //현재 체크박스가 체크가 되어 있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false; //no버튼 클릭시 다시 돌아감.
        }//삭제if
        //모든 체크박스를 가져오기
        $(".stuChk").each(function(){
            if($(this).is(":checked") == true ){
                console.log("현재 선택된 class 값 : "+$(this).val());
                console.log("현재 선택된 id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//each
    });//하단삭제버튼
});//제이쿼리