import axios from "axios";
import React, {useEffect, useState} from "react";

// import RekursButton from "../RekursButton";
import RecursSelect from "./RecursSelect";
import {connect} from 'react-redux'

import { useSelector } from "react-redux";

import './Modal.scss'

function ClassificationShtdn (props, isOpen) {
  
    const classifications = useSelector(state=>state.classificationDataReducer)
    const [views, setViews] = useState('')    
    const [data, setData] = useState('<p>f</p>')
    

    let datas = ''
    if( views){
        datas = (<select >
                {Object.keys(views).map((data_name)=>{
                    return Object.keys(views[data_name]).map((el)=>{
                        return Object.keys(views[data_name][el]).map((key)=>{
                            
                            if(isNaN(Number(views[data_name][el][key]))){
                                return <option>{views[data_name][el][key]}</option>
                            }
                        })
                    })
                })}
            </select>)
        
     
    }
    
    function handleRequest(){
        console.log(classifications)
        console.log(classifications['id'])
        let id_record = classifications['id']
        console.log(id_record)
        // classifications['flag_classification'] = true
        // let put_url =  'http://technolog.bzf.asu/shutdown/shutdowndetail/'
        let put_url =  'http://10.21.10.12:8000/shutdown/shutdowndetail/'
        
        axios.put(put_url, {
            classifications,
        }).then((response)=>{console.log(response)})
        props.closeModal()
    }
 

    return (

        <div className="modal-in">
            <div className="init-info">
            {props.obj['id']}
                <p>{props.obj['Начало простоя']} начался простой</p>
                <p> на {props.obj['Название агрегата']}</p> 
                <p>закончился  {props.obj['Окончание простоя']}</p>
                <p> продолжительность простоя составила: {props.obj['продолжительность']}</p>
                <p>Произведите классификацию простоя:</p> 
            </div>
            
        <RecursSelect idRecord={props.obj['id']} lvl={0}/>
        <button onClick={handleRequest} >Записать данные  </button>
        </div>
        
    )



}
export default connect()(ClassificationShtdn)