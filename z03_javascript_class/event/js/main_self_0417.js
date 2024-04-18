$(function(){
    let com_cnt = 0;
    let now = new Date;
    today = now.getFullYear()+'-'+now.getMonth()+'-'+now.getDate();


    //-----------------------------------------------새로입력 시작----------------------------------//
    $(document).on("click",".replyBtn",function(){
        
        com_cnt ++;
        event.preventDefault()
        console.log(today);
        let ccont = $(".replyType").val()
        let h_data = "";
        h_data+='<ul id='+com_cnt+'>'
        h_data+='<li class="name">aaa<span>['+today+'&nbsp;&nbsp;15:01:59]</span></li>'
        h_data+='<li class="txt">'+ccont+'</li>'
        h_data+='<li class="btn">'
        h_data+='<a href="#" class="rebtn updateBtn">수정</a>'
        h_data+='<a href="#" class="rebtn delBtn">삭제</a>'
        h_data+='</li>'
        h_data+='</ul>'
        $(".replyBox").prepend(h_data); 
    });// .replyBtn
    

    //-----------------------------------------------새로입력 끝----------------------------------//



    //-----------------------------------------------불러오기 시작----------------------------------//
    $.ajax({
        url:"http://127.0.0.1:5500/javascript_class/event/event/json/comment_data.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            //alert('success');
            let h_data = "";
            for(let i=0;i<data.length;i++){
                h_data+='<ul id='+data[i].cno+'>'
                h_data+='<li class="name">'+data[i].id+' <span>['+data[i].cdate+'&nbsp;&nbsp;15:01:59]</span></li>'
                if(data[i].id == "aaa"){

                    h_data+='<li class="txt">'+data[i].ccont+'</li>'
                    h_data+='<li class="btn">'
                    h_data+='<a href="#" class="rebtn updateBtn">수정</a>'
                    h_data+='<a href="#" class="rebtn delBtn">삭제</a>'
                    h_data+='</li>'
                }
                else{
                    
					h_data+='<li class="txt">'
					h_data+='<a href="password.html" class="passwordBtn"><span class="orange">※ 비밀글입니다.</span></a>'
					h_data+='</li>'
                }
                h_data+='</ul>'
            }
            $(".replyBox").html(h_data); 
            com_cnt = h_data.length;
        },
        error:function(data){
            alert('error');
        } 
    });//ajax
    //-----------------------------------------------불러오기 끝----------------------------------//


});// query