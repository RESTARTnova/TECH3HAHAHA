import axios from 'axios'
import React, {useState, useEffect} from "react"
import moment from 'moment'
import PeriodInput from '../PeriodInput.js'
import Filter from '../Filters/Filter.js'

import {useSelector, connect} from 'react-redux'

import './ShootdownEquipment.scss'

import Modal from 'react-modal'
import ClassificationShtdn from './ModalClass/ModalClass.js'







function ShootdownEquipment() {
  const [stop, setStop] = useState(true)
  const datePeriod = useSelector(state=>state.periodReducer) // 

  const[post, setPost] = useState(null)
  const [modal, setModal] = useState({obj:{}, state:false})
 
  useEffect(() => {
    // axios.post('http://technolog.bzf.asu/shutdown/get_shutdowns/' ,{
    axios.post('http://10.21.10.12:8000/shutdown/get_shutdowns/', {
      test: 'test',
      date_begin: datePeriod.dateBegin,
      date_end: datePeriod.dateEnd
    }
    ).then((response)=>{
      setPost(()=>{return {'Shutdowns': response.data['Shutdowns'].sort((a,b)=>{
        let da = new Date(a['Окончание простоя'])
        let db = new Date(b['Окончание простоя'])
        return  db-da
      })}})
    })
  },[stop])
  
  const openModal = ()=>{setModal(true)}
  const closeModal = ()=>{
    setStop(!stop)
    setModal({obj:{}, state:false})}


  const handleClckClass = (obj)=>{
    setModal({obj: obj, state:true })
    console.log('Типа пошли куда то, форму вызвали ' + 'modal = ')
    
  }
  const handleDatePeriodClick = () => {
    console.log('helo from handleDatePeriodClick '+ datePeriod.dateBegin + '-' +datePeriod.dateEnd)
    if (datePeriod.dateBegin !== '' && datePeriod.dateEnd !==''){
      if(Date.parse(datePeriod.dateBegin)<=Date.parse(datePeriod.dateEnd)){
        // axios.post('http://technolog.bzf.asu/shutdown/get_shutdowns/', {
        axios.post('http://10.21.10.12:8000/shutdown/get_shutdowns/', {
      
            date_begin: datePeriod.dateBegin,
            date_end: datePeriod.dateEnd}).then((response)=>{
              setPost(()=>{return {'Shutdowns': response.data['Shutdowns'].sort((a,b)=>{
                let da = new Date(a['Окончание простоя'])
                let db = new Date(b['Окончание простоя'])
                return  db-da
              })}})
            })
      }
    }
  }
  function forFilter (name, data){
    let arr=[]
    Object.keys(data).map((e)=>{
        if(!arr.includes(data[e][name] )&& data[e][name]!=null){
          arr.push(data[e][name])
          console.log(name+' - '+data[e][name])
        }
         
        
      
    })
    

    return arr
  }
  function handleModal(){
    setModal({obj:{}, state:false})
    setStop(!stop)
  }

  let result, head_res
  
  if(!post) return null
    
  else if (post['Shutdowns']){


    head_res = Object.keys(post).map((el)=>{
      let head
      return(
        <tr>
          {head = Object.keys(post[el][0]).map((i)=>{ 
            if(i==='id') return null
            if (i==='Начало простоя' || i==='Окончание простоя' || i==='продолжительность' )           
              return <td>{i}</td>  //сюда надо вставить sellect для фильтров, кроме дат номеров, подобрать фильтр для продолжительности
                                   //Это будет жёстко
            if (i==='Классификация')
              return (<td> {<Filter arr={['Классифицирован','Не классифицирован']}name={i}/>}</td>)
            
            return (<td> {<Filter arr={forFilter(i, post[el])}name={i}/>}</td>)// Это было не жёстко, это еб вашу мать было АЦКИ Нереально ЖЁСТКО
          })}
        </tr>
      )      
    })
    result = Object.keys(post).map((el)=>{
        el = post[el].map((obj)=>{
        let el_i
        return(
            <tr className="string">{
              el_i = Object.keys(post[el][0]).map((i)=>{
                if (String(obj[i])=== 'true' && i==='Классификация') 
                    return(
                        <td className="field_my">&#128504;</td>
                    )
                else if (String(obj[i])=== 'false' && i==='Классификация')
                  return(
                    <td className="field_my" style={{padding: '0px 0px 0px 0px', width: 'auto', height: 'auto'}}>
                        <button className='classBtn' onClick={()=>{handleClckClass(obj)}}>класифицировать!?</button>
                    </td>
                  )
                else if (i==='id')
                {return null} 
                return(
                    <td className="field_my">
                        {obj[i]}
                    </td>
                )
              })
            }</tr>
        )
        })
        return el 
    })}
  return (
  <div className='shutdowns'>
    <Modal className="modal" isOpen={modal.state} onRequestClose={closeModal} ariaHideApp={false}>
      <button className='closeModal' onClick={closeModal}>X</button>
      <ClassificationShtdn obj={modal.obj} closeModal={handleModal}/>
      
      
    </Modal>
    <span>{datePeriod.value}</span>
    <div className='alterPeriod'>
     
      <PeriodInput onFullChange = {handleDatePeriodClick}/>
      {/* <input type='date' value={DateNow()['now_day']}/> */}
      <label>Задайте альтернативный период</label>
    </div>
    
    <input type='button' value={'Классификация простоев'}/>
    <input type='button' value={'Получить отчёт'}/>
    <div className='table-of-result'>
    <table>
      <thead>{head_res}</thead>
    
        <tbody  className='tbody-of-result'>{result}</tbody>
      </table>
    </div>  

    
  </div>)
 
   
}
export default connect()(ShootdownEquipment)