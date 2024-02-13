import React from 'react';
import {putEnd, putBegin} from '../store/dateGetter/dateGetter.js'
import { useDispatch} from 'react-redux'

// Стили для даты
import './DatePickerNowStyle.scss'

const DatePickerNow = (props) => {
  
  const dispatch = useDispatch()
  // const dateSelect = useSelector(state=>state.periodReducer)

  let dflt = new Date() //получаем текущую дату
  let year = dflt.getFullYear().toString() // получаем из текущей даты год, месяц и день
  // let month = dflt.getMonth()+1
  let month = ()=>{
    if(dflt.getMonth()<9){
      return '0'+(dflt.getMonth()+1)
    }
    else {
      return (dflt.getMonth()+1).toString()
    }
  }
  let day = ()=>{ // проверяем переданный параметр "0" для первого числа сего месяца, и преобразуем первые числа месяца, добавляя "0" впереди для формата
    if(props['f']=== '0')
    {
      return '01'
    } 
    else {
      if (dflt.getDate()<10)
        {return '0'+dflt.getDate().toString()}
      else
        {return dflt.getDate()}
      }
    }
  const date = year+'-'+month()+'-'+day();//составляем дефолтное состояние date
 
  
 

  
  const handleChange = (e) => { // Складываем даты в store

    if (props['f']=='0')
    {
      dispatch(putBegin({begin: e.target.value.toString()}))
    }
    else {dispatch(putEnd({end: e.target.value.toString()}))}
    
  };


  
  return (
    <div className='datePickerStyle'>
      <input
        type="date"
        onChange={handleChange}
 
        defaultValue = {date} 
        
      />
      {/* <p>Выбранная дата: {date}</p> */}
    </div>
  );
};

export default DatePickerNow;