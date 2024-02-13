import React, {useEffect, useState} from "react";
import axios from 'axios'
import  './Tpm.scss'
import decodeTable from '../TablleDecoder/TableDecoder'
import DatePickerNow from "../DatePicker";

export default function Tpm(){

    const [post, setPost] = useState(null)
    
    // let head_res,result,head,el_i

        // useEffect(() => {
        //     const fetchData = () =>{
        //         // axios.get('http://technolog.bzf.asu/tpm/get_fault/').then(postData => {
        //         // axios.get('http://technolog.bzf.asu/tpm/get_fault/').then((response) => {
        //         // axios.get('http://localhost:8000/tpm/get_fault/').then((response) => {
        //          setPost(response.data)
        //         //  console.log(data.keys[0])
        //         })
        //        }
        //        fetchData()
        // },[])
        
    // if(!post)
    //     return null
    // else{
        // let result = Object.keys(post).map((el)=>{
        //     el = post[el].map((obj)=>{
        //         function fuck() {
        //             let a_in = []
        //             for (let i in Object.keys(obj))
        //             {
        //                 a_in.push(obj[Object.keys(obj)[i]])
        //                 // console.log(obj)
        //             }
        //             return(
        //                 a_in
        //             )
        //         }
        //         a.push(fuck())
                
        //         return (
        //             <tbody>
        //                 <tr>
        //                     <td>{obj.id}</td>
        //                     <td>{obj.data_time}</td>
        //                     <td>{obj.user}</td>
        //                     <td>{obj.rfid}</td>
        //                     <td>{obj.fault}</td>
        //                     <td>{obj.tag}</td>
        //                 </tr>
        //             </tbody>
        //         )
        //     })
        //     return el 
        // })
        // head_res = Object.keys(post).map((el)=>{
        //     let head
        //     return(
        //       <tr>
        //         {head = Object.keys(post[el][0]).map((i)=>{            
        //           return (<td> {i}</td>)
        //         })}
        //       </tr>
        //     )      
        //   })
        //   result = Object.keys(post).map((el)=>{
        //       el = post[el].map((obj)=>{
        //       let el_i
        //       return(
        //           <tr className="string">{
        //             el_i = Object.keys(post[el][0]).map((i)=>{
        //               if (String(obj[i])=== 'true') 
        //                   return(
        //                       <td className="field_my">
        //                           &#128504;
        //                       </td>
        //                   ) 
        //               return(
        //                   <td className="field_my">
        //                       {obj[i]}
        //                   </td>
        //               )
        //             })
        //           }</tr>
        //       )
        //       })
        //       return el 
        //   })
        console.log('Working3')
        return (
            <div className="tpm">
                <div className="upperContainer">
                    <div className="searchContainerMain">
                        <div className="textSearch">
                            <p className="textDate">Поиск</p>
                        </div>
                        <div className="searchContainer">
                            <input className="searchStyle" placeholder="Поиск по оборудованию" type="text" name="search"/>
                        </div>
                    </div>
                    <div className="dateContainer">
                        <div className="textDateContainer">
                            <p className="textDate">Дата</p>
                        </div>
                        <div className="filterDateContainer">
                            <div className="beforeDateContainer">
                                <p className="textDateS">С</p>
                                <DatePickerNow f='0'/>
                            </div>
                            <div className="afterDateContainer">
                                <p className="textDatePo">По</p>
                                <DatePickerNow f='1'/>
                            </div>
                        </div>
                    </div>
                </div>
                <div className='mainContainer'>
                    <p>Text</p>
                </div>
            </div>
        ) 
    }
// }