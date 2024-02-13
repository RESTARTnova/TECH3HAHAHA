import React, { useRef, useState, useEffect } from 'react';
import DatePickerNow from './DatePicker.js'
import './PeriodInput.scss'



// import {useSelector, useDispatch} from 'react-redux'
// import {testik, getDate, nullDate} from '../store/dateGetter/dateGetter.js'
// import getDate 

export default function PeriodInput (props) {


    return (
        <div className='periodInput'>
            <p>C</p>
            <DatePickerNow f='0'/>
            <p>До</p>
            <DatePickerNow f='1'/>
            <button className='inputDate' type="button" onClick={props.onFullChange} >Получить данные за выбранный период</button>
        </div>
    )
}