import React from "react"
import './TableDecoder.scss'
import {ExportToExcel} from '../tpm/ExportToExcel'

export default function decodeTable(post,save_file_name){ {/*Запихивать сюды любой JSON формата {key:[ {ключи:значения},
                                                                                        {}]} и получите табличку
                                                                                    ДА, Это велосипед наверняка!!!, 
                                                                                Но это мой велосипед!!!!*/}

let save_param_values = []
let save_param_headers = []
let save_param_headers_not_common = []
let save_param_values_not_common = []
let head_res
if(!post) return null

else{
    // // Создание excel файла
    // const customHeadings = post.filtered_faults.map((item)=>({
    //     "№ записи": item.id,
    //   "Время": item.data_time,
    //   "Обходчик": item.user,
    //   "Отчёт": item.fault,
    //  // отформатированная строка: "Отчёт": item.fault.split("%")[1],
    //   "Машина": item.rfid,
    //   "Тег": item.tag
    // }))
let result = Object.keys(post).map((el)=>{
    // console.log('Object.keys(post) = ' + Object.keys(post))
    // console.log('Object.keys(post[el][0]) = ' + Object.keys(post[el][0]))
    el = post[el].map((obj)=>{
    let el_i
    return(
        <tr className="string">
        {/* Надо это как то превратить в цикл типа нечто.map((key)=>{return obj.key}) */}
            {
            el_i = Object.keys(post[el][0]).map((i)=>{
                // console.log(i)
                // console.log(obj[i])

                if (String(obj[i]).includes('T') && String(obj[i]).includes('Z')){
                    obj[i] = String(obj[i]).split('.')[0].replace('T','/');
                }

                save_param_headers.push(i)
                save_param_values.push(obj[i])

                if (String(obj[i]).includes('%')) 
                    return(
                        <td className="field_my">
                            {String(obj[i]).split('%')[1]}
                        </td>
                    )
                      

                if (String(obj[i])=== 'true') 
                    return(
                        <td className="field_my">
                            &#128504;
                        </td>
                    )
                        
                return(
                    <td className="field_my">
                        {obj[i]}
                    </td>
                )//Теперь мне не надо знать ключи Json, он их сам выкавыривает и юзает
                // ебать я гений
                // Универсальнейшея вещь }:|)
                // Арррааарргх ..... (типа смех злого гения)
            })
            
            }
        </tr>
    )
    })
    return el 
})
// Работает для заголовков. Фильтрация для уникальных значений.
for (let j = -1;j < save_param_headers_not_common.length;j++){
    if (!save_param_headers_not_common.includes(save_param_headers[j])){
        save_param_headers_not_common.push(save_param_headers[j])
    }
}
let save_param = []
let last_position = 0
let j =0
save_param_headers_not_common.shift()
// console.log(save_param_headers_not_common)
save_param.push(save_param_headers_not_common)
// Работает для данных. Фильтрация для нужного вида.
for (let i = 0; i <save_param_values.length / save_param_headers_not_common.length; i++){
    save_param_values_not_common = []
    for(j = 0;j<save_param_headers_not_common.length;j++){
        save_param_values_not_common.push(save_param_values[last_position +j])
        // console.log(save_param_values)
    }
    last_position += j
    save_param.push(save_param_values_not_common)
}
head_res = Object.keys(post).map((el)=>{
    let head
    return(
      <tr>
        {head = Object.keys(post[el][0]).map((i)=>{            
          return (<td> {i}</td>)
        })}
      </tr>
    )      
  })
// console.log(save_param)
return( <>
    <table className="table_style">
        <thead className="table_head">{head_res}</thead>
        <tbody className="table_body">{result}</tbody>
    </table>
    <ExportToExcel apiData={save_param} fileName={save_file_name} />
    </>)
}
}
