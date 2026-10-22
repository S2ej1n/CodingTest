function solution(new_id) {
    var answer = '';
    tec = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
    // '~'||'!'||'@'||'#'||'$'||'%'||'^'||'&'||'*'||'('||')'||'='||'+'||'['||'{'||']'||'}'||':'||'?'||','||'<'||'>'||'/'
    
    // 1.
    new_id = new_id.toLowerCase();
    
    // 2. 허용 외 모든 문자 제거 ~!@#$%^&*()=+[{]}:?,<>/
    // for(let j of tec){
    //     if(new_id.includes(j)){
    //         new_id = new_id.replaceAll(j,'')
    //     }
    // }
    
    new_id = new_id.replace(/[^a-z0-9-._]/g,'')
    
    // let stack = [new_id[0]]
    // 3. 2번이상 연속.
//     for(let i = 1; i < new_id.length; i++){
//         if(new_id[i] == '.' && stack[stack.length-1] == new_id[i]){
//             continue;
//         }else{
//             stack.push(new_id[i])
//         }
//     }
    
//     new_id = stack.join('')
    
    new_id = new_id.replace(/\.{2,}/g,'.')
    
    // 4.
    if(new_id.startsWith('.')){
        new_id = new_id.slice(1)
    }
    if(new_id.endsWith('.')){
        new_id = new_id.slice(0,new_id.length - 1)
    }
    
    //5.
    if(new_id==''){new_id = 'a'}
    
    if(new_id.length >= 16){
        new_id = new_id.slice(0,15)
        if(new_id.endsWith('.')){
            new_id = new_id.slice(0,new_id.length - 1)
        }
    }
    
    if(new_id.length <= 2){
        while(new_id.length < 3){
            new_id += new_id[new_id.length - 1].repeat(3 - new_id.length)
        }
    }
    
    return new_id;
}