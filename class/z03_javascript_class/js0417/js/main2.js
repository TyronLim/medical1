$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];
    
    let t_maker = "";
    for(let i=0;i<no.length;i++){
        t_maker+="<tr id='"+no[i]+"'>"
        t_maker+="<td> <input type='checkbox' name='td"+no[i]+"' class='each_chk'  value='"+no[i]+"'></td>"
        t_maker+="<td id='no"+no[i]+"'>"+no[i]+"</td>"
        t_maker+="<td id='na"+no[i]+"'>"+name[i]+"</td>"
        t_maker+="<td id='ko"+no[i]+"'>"+kor[i]+"</td>"
        t_maker+="<td id='en"+no[i]+"'>"+eng[i]+"</td>"
        t_maker+="<td id='ma"+no[i]+"'>"+math[i]+"</td>"
        t_maker+="<td id='to"+no[i]+"'>"+total[i]+"</td>"
        t_maker+="<td id='av"+no[i]+"'>"+avg[i]+"</td>"
        t_maker+="<td id='ra"+no[i]+"'>0</td>"
        t_maker+="<td><button class='delBtn'>삭제</button></td>"
        t_maker+="</tr>" 
    }

    $("#t_body").html(t_maker);
    
    $(document).on("click",".delBtn",function(){
        //console.log($(this).parent().parent().attr('id'));
        if(confirm('삭제하시겠습니까?')){
        $('#'+$(this).parent().parent().attr('id')).remove();
        }
    });//delBtn 
    
    // $(".delBtn").click(function(){
    //     //console.log($(this).parent().parent().attr('id'));
    //     if(confirm('삭제하시겠습니까?')){
    //     $('#'+$(this).parent().parent().attr('id')).remove();
    //     }
    // });//delBtn 

    $("#deleteBtn").click(function(){
        $(".each_chk").each(function(){
            if($(this).is(":checked")==true){
                //console.log($(this).parent().parent().attr('id'))
                if(confirm('삭제하시겠습니까?')){
                    $('#'+$(this).parent().parent().attr('id')).remove()
                };
            };
        });
    });//deleteBtn

    $('#allChk').click(function(){
        if($(this).is(':checked')==true){
            $(".each_chk").each(function(){
                $(this).prop("checked",true)
            })
        }
        else{
            $('.each_chk').each(function(){
                $(this).prop("checked",false)
            })
        }
    });//allChk

    $(".each_chk").click(function(){
        //console.log($(this).parent().parent().attr('id'));
        //$(this).parent().parent().attr('id')
    });//each_chk

    $("#add_ok_btn").click(function(){
        if($("#add_name").val().length<2){
            alert('이름을 정확히 입력해주세요.');
            $("#add_name").focus();
            return false;
        }
        let n_number = Math.max.apply(null,no)+1;
        no.push(n_number);
        let n_name=$("#add_name").val();
        let n_kor=Number($("#add_kor").val());
        let n_eng=Number($("#add_eng").val());
        let n_math=Number($("#add_math").val());
        let n_total=n_kor+n_eng+n_math;
        let n_avg=(n_total/3).toFixed(2);


        let add_t_maker = "";
        //console.log($("#add_name").val())
        //console.log($("#add_kor").val())
        //console.log($("#add_eng").val())
        //console.log($("#add_math").val())
        add_t_maker+="<tr id='"+n_number+"'>"
        add_t_maker+="<td> <input type='checkbox' name='td"+n_number+"' class='each_chk'  value='"+n_number+"'></td>"
        add_t_maker+="<td>"+n_number+"</td>"
        add_t_maker+="<td>"+$("#add_name").val()+"</td>"
        add_t_maker+="<td>"+$("#add_kor").val()+"</td>"
        add_t_maker+="<td>"+$("#add_eng").val()+"</td>"
        add_t_maker+="<td>"+$("#add_math").val()+"</td>"
        add_t_maker+="<td>"+n_total+"</td>"
        add_t_maker+="<td>"+n_avg+"</td>"
        add_t_maker+="<td>0</td>"
        add_t_maker+="<td><button class='delBtn'>삭제</button></td>"
        add_t_maker+="</tr>" 
        $('#t_body').append(add_t_maker);
        $("#add_name").val("")
        $("#add_kor").val("")
        $("#add_eng").val("")
        $("#add_math").val("")
        $("#add_all_window").css('display','none');

    });//add_ok_btn


    // 입력 버튼
    $("#writeBtn").click(function(){
        $("#add_all_window").css('display','block');
    });//writeBtn
    
    $("#add_no_btn").click(function(){
        $("#add_all_window").css('display','none');
    });//add_no_btn


    // 검색 버튼
    $("#searchBtn").click(function(){
        $("#search_all_window").css('display','block');
    })//searchBtn

    
    $("#search_ok_btn").click(function(){
        //console.log($("#search_txt").val());
        for(let i=0;i<name.length;i++){
            if(name[i]==$("#search_txt").val()){
                
                $("#search_all_window").css('display','none');
                //console.log($("#n"+(i+1)));
                let sear_t_maker = "";

                sear_t_maker+="<tr id='"+no[i]+"'>"
                sear_t_maker+="<td> <input type='checkbox' name='td"+no[i]+"' class='each_chk'  value='"+no[i]+"'></td>"
                sear_t_maker+="<td id='no"+no[i]+"'>"+no[i]+"</td>"
                sear_t_maker+="<td id='na"+no[i]+"'>"+name[i]+"</td>"
                sear_t_maker+="<td id='ko"+no[i]+"'>"+kor[i]+"</td>"
                sear_t_maker+="<td id='en"+no[i]+"'>"+eng[i]+"</td>"
                sear_t_maker+="<td id='ma"+no[i]+"'>"+math[i]+"</td>"
                sear_t_maker+="<td id='to"+no[i]+"'>"+total[i]+"</td>"
                sear_t_maker+="<td id='av"+no[i]+"'>"+avg[i]+"</td>"
                sear_t_maker+="<td id='ra"+no[i]+"'>0</td>"
                sear_t_maker+="<td><button class='delBtn'>삭제</button></td>"
                sear_t_maker+="</tr>" 

                $("#t_body").html(sear_t_maker);
            }
        }
    });//search_ok_btn
    
    $("#search_no_btn").click(function(){
        $("#search_all_window").css('display','none');
    })//search_no_btn


    // 수정 버튼
    $("#modifyBtn").click(function(){
        $("#chan_all_window").css('display','block');
    })//modifyBtn

    $("#chan_no_btn").click(function(){
        $("#chan_all_window").css('display','none');
    })//chan_no_btn

    $("#chan_ok_btn").click(function(){
        $
    })//chan_ok_btn


}); //query