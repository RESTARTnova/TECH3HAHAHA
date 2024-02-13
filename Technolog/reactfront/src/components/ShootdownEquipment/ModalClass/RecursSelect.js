import axios from 'axios'
import React, {useState, useEffect} from 'react'
import {connect} from 'react-redux'
import './Modal.scss'
import { putClassStdn, putTypeStdn, putFactStdn , put_id, putFlag} from '../../../store/ClassificationData/ClassificationData'
import { useDispatch } from 'react-redux'

function RecursSelect(props){

    const dispatch = useDispatch()
    let label = ['Выберете класс простоя', 'Выберете вид простоя', 'Выберете фактор простоя',]
  
    const [arr, setArr] = useState()
    const [ischange, setIsChange] = useState(false) 
    const [element, setElement] = useState(null)
    const [id, setId] = useState(0)
    const [selectValue, setSelect] = useState('init')
   
    useEffect(()=>{
        setElement(null)
        if (props.lvl==0){
            dispatch(put_id({
                id : props.idRecord
            }))
        }
        axios.post('http://technolog.bzf.asu/shutdown/get_class_shutdowns/', {
        // axios.post('http://10.21.10.12:8000/shutdown/get_class_shutdowns/', {
            model: props.model,
            change: props.change,
            lvl: props.lvl,
        })

        .then((response)=>{setArr(response.data)})

    },[props.change])
    let datas=''
    if (arr && Object.keys(arr).length>0){
        
        
        datas = (<div className='recursion-select'>
                    <label className='label-select'>{label[props.lvl]}</label>
                    <select value={selectValue} onChange={(e)=>{

                        setElement(null)
                        setIsChange(true)
                       
                        handleChange(e, id)}}>
                        <option value='init' selected></option>
                        {Object.keys(arr).map((data_name)=>{
                            return Object.keys(arr[data_name]).map((el)=>{
                                return Object.keys(arr[data_name][el]).map((key)=>{
                                   
                                    if(isNaN(Number(arr[data_name][el][key]))){
                                        
                                        return <option id={el+1} value={arr[data_name][el][key]}>{arr[data_name][el][key]}</option>
                                    }
                                })
                            })
                        })}
                    </select></div>)
        
    }
    else return null

    function handleChange(e){
        
        if (e.target.value){
            setSelect(e.target.value)
        }
        else setSelect('init')
           
        if (!ischange ){
            setIsChange(false)
            if(props.lvl==0){
               
                dispatch(putClassStdn({
                    
                    value:e.target.value
                }))
            }
            if(props.lvl==1){
                dispatch(putTypeStdn({
                    value:e.target.value
                }))
            }
            if(props.lvl==2){
                dispatch(putFactStdn({
                    value:e.target.value
                }))
                dispatch(putFlag({
                    flag:true
                }))
            }
            
            setElement(()=>{
                console.log('рекурсия отработала '+ props.lvl+ ' раз')
                return <RecursSelect lvl={props.lvl+1} change={e.target.value} model={Object.keys(arr)[0]}/>
            })
        }
        else{
            setIsChange(true)
        }
    }
    
    return <div className='pop-up' >
        {datas}
        {element}
    </div> 


}

export default RecursSelect