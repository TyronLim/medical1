// ajax stu_score 10개의 데이터를 출력하시오.
// 학생입력 -> 학생추가 프로그램 구성
// 학생수정 -> 학생성적수정 가능하게 구성
// 학생삭제 -> 선택된 학생이 삭제되도록 구성

$(function(){
    let stu_no = 0;

    //------------------------------------  학생삭제(개별) 시작  -----------------------------------------//
    //$('.delBtn').click(function(){
    $(document).on('click','.delBtn',function(){
        //alert('test');
        //console.log($(this).parent().prev().prev().prev().prev().prev().prev().prev().text());
        conf_name = $(this).parent().prev().prev().prev().prev().prev().prev().prev().text();
        //console.log(conf_name);
        if(confirm('선택하신 <'+conf_name+'>학생을 삭제하시겠습니까?')){
            $(this).parent().parent().remove();
        }
        else{
            return false;
        }

    });//delBtn
    
    //------------------------------------  학생삭제(개별) 시작  -----------------------------------------//
    
    //------------------------------------  학생삭제(체크된) 시작  -----------------------------------------//
    $("#deleteBtn").click(function(){
        if($(".stuChk:checked").length==0){
            alert('삭제할 학생을 체크해주세요');
        }
        else{
            $(".stuChk:checked").each(function(){
                if(confirm('삭제하시겠습니까?')){
                    $(this).parent().parent().remove();
                }
                else{
                    return false;
                }
            });
        }
    });//deleteBtn

    //------------------------------------  학생삭제(체크된) 끝  -----------------------------------------//

    //------------------------------------  학생수정 시작 -----------------------------------------//
    $("#modifyBtn").click(function(){
        if($(".stuChk:checked").length!=1){
            alert('한 명의 학생을 체크해주세요.');
        }
        else{
            let show_name = $(".stuChk:checked").parent().next().next().text();
            let show_kor = $(".stuChk:checked").parent().next().next().next().text();
            let show_eng = $(".stuChk:checked").parent().next().next().next().next().text();
            let show_math = $(".stuChk:checked").parent().next().next().next().next().next().text();
            //console.log(update_no);
            //console.log(update_name);
            $(".p_all").css('display','block');
            $("#name").prop("readonly",true);
            
            $("#name").val(show_name);
            $("#kor").val(show_kor);
            $("#eng").val(show_eng);
            $("#math").val(show_math);
            
            $("#cancelBtn").click(function(){
                $(".p_all").css('display','none');
            });//cancelBtn
            
            
        };
    });//modifyBtn

    //------------------------------------  학생수정 끝  -----------------------------------------//

    //------------------------------------  학생입력 시작  -----------------------------------------//
    $("#writeBtn").click(function(){
        if($(".stuChk:checked").length != 0){
            alert('학생에 체크가 되어 있습니다. 체크를 해제합니다. \n다시 시도해주세요.')
            $(".stuChk").each(function(){
                $(this).prop('checked',false);
            });
        }
        else{
            $(".p_all").css('display','block');

            $("#name").prop("readonly",false);

            $("#confirmBtn").click(function(){
                if($(".stuChk:checked").length==0){
                    stu_no ++;
                    let insert_name = $("#name").val();
                    let insert_kor = Number($("#kor").val());
                    let insert_eng = Number($("#eng").val());
                    let insert_math = Number($("#math").val());
                    let insert_total = insert_kor + insert_eng + insert_math
                    let insert_avg = insert_total/3
                    let h_data = ""
                    h_data += "<tr id="+stu_no+">";
                    h_data += "<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                    h_data += "<td>"+stu_no+"</td>";
                    h_data += "<td>"+insert_name+"</td>";
                    h_data += "<td>"+insert_kor+"</td>";
                    h_data += "<td>"+insert_eng+"</td>";
                    h_data += "<td>"+insert_math+"</td>";
                    h_data += "<td>"+insert_total+"</td>";
                    h_data += "<td>"+insert_avg+"</td>";
                    h_data += "<td>"+0+"</td>";
                    h_data += "<td><button class='delBtn'>삭제</button></td>";
                    h_data += "</tr>";
                    $("#body").append(h_data);
                    alert('학생정보가 저장되었습니다.')
                    $("#name").val("");
                    $("#kor").val("");
                    $("#eng").val("");
                    $("#math").val("");
                    $(".p_all").css('display','none');
                }
                else{
                    $("#confirmBtn").click(function(){
                        //console.log($(".stuChk:checked").parent().parent().attr('id'));
                        
                        let update_no = $(".stuChk:checked").parent().parent().attr("id");
                        let update_name = $("#name").val();
                        let update_kor = Number($("#kor").val());
                        let update_eng = Number($("#eng").val());
                        let update_math = Number($("#math").val());
                        let update_total = update_kor + update_eng + update_math;
                        let update_avg = update_total/3;
                        
                        let up_data = ""
                        up_data += "<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                        up_data += "<td>"+update_no+"</td>";
                        up_data += "<td>"+update_name+"</td>";
                        up_data += "<td>"+update_kor+"</td>";
                        up_data += "<td>"+update_eng+"</td>";
                        up_data += "<td>"+update_math+"</td>";
                        up_data += "<td>"+update_total+"</td>";
                        up_data += "<td>"+update_avg+"</td>";
                        up_data += "<td>"+0+"</td>";
                        up_data += "<td><button class='delBtn'>삭제</button></td>";

                        $(".stuChk:checked").parent().parent().html(up_data)
                        alert('수정이 완료되었습니다.')
                        $("#name").val("");
                        $("#kor").val("");
                        $("#eng").val("");
                        $("#math").val("");
                        $(".p_all").css("display","none");

                    });//수정>확인
                }

            });//confirmBtn

            $("#cancelBtn").click(function(){
                $(".p_all").css('display','none');
            });//cancelBtn
        }
    });//writeBtn
    //------------------------------------  학생입력 끝  -----------------------------------------//


    //------------------------------------  불러오기 시작  -----------------------------------------//
    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            //alert('성공');
            h_data = ""
            for(let i=0; i<10; i++){
                h_data += "<tr id="+data[i].no+">";
                h_data += "<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                h_data += "<td>"+data[i].no+"</td>";
                h_data += "<td>"+data[i].name+"</td>";
                h_data += "<td>"+data[i].kor+"</td>";
                h_data += "<td>"+data[i].eng+"</td>";
                h_data += "<td>"+data[i].math+"</td>";
                h_data += "<td>"+data[i].total+"</td>";
                h_data += "<td>"+data[i].avg+"</td>";
                h_data += "<td>"+data[i].rank+"</td>";
                h_data += "<td><button class='delBtn'>삭제</button></td>";
                h_data += "</tr>";
            }
            $("#body").html(h_data);
            stu_no = 10;
        },
        error:function(data){
            alert('실패');
        }
    });//ajax
    //------------------------------------  불러오기 끝  -----------------------------------------//
});//jquery

                    
                    
                   