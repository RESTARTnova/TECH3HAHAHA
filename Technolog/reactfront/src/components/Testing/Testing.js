import React, {useEffect, useState} from "react";
import axios from 'axios'
import './Testing.scss'
// import {ExportToExcel} from './ExportToExcel'

export default function Testing(){


    const [post, setPost] = useState(null)
    const [post_f, setPost_f] = useState(null)

   
   

    console.log('gshfjk1')
    useEffect(() => {
        // axios.get('http://technolog.bzf.asu/testing/foreign_key/').then((response)=>{
        axios.get('http://localhost:8000/testing/foreign_key/').then((response)=>{
          setPost(response.data)
        })
        axios.get('http://localhost:8000/testing/foreign_key_f/').then((response)=>{
          setPost_f(response.data)
        })
      },[])


    if(!post || !post_f)
        return null
    else{
        console.log('gshfjk')
        let result = Object.keys(post).map((el)=>{
            el = post[el].map((obj)=>{
                console.log(obj.id)
                
                return (
                    
                        <tr>
                            <td>{obj.id}</td>
                            <td>{obj.name_f}</td>
                            <td>{obj.number_f}</td>
                            <td>{obj.foreign_key_test}</td>
                            
                        </tr>
                    
                )
            })
            return el 
        }) 
        let result_f = Object.keys(post_f).map((el)=>{
            el = post_f[el].map((obj)=>{
                console.log(obj.id)
                
                return (
                    
                        <tr>
                            <td>{obj.id}</td>
                            <td key={obj.name}>{obj.name}</td>
                            <td>{obj.number}</td>
                            
                            
                        </tr>
                    
                )
            })
            return el 
        })
   
        return (
            <div className="testing">
                <div className="lowtable">
                {result}
                </div>
                <div className="uptable">{result_f}</div>
                    
                    
            </div>
        ) 
    }
}