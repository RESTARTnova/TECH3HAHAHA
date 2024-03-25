import React, {useEffect, useState} from "react";
import axios from 'axios'
import  './Tpm.scss'
import DatePickerNow from "../DatePicker";
import { useSelector } from 'react-redux';
import ReactModal from 'react-modal';
import ModalClass from "./ModalClass";
import { Test } from "./NewExcel";

export default function Tpm(){

    
    const [renderModal, setRenderModal] = useState(false);
    
    const manageRender = () => {
        setRenderModal(!renderModal)
    }
    
    const [excel,setExcel] = useState('');
    const [excelName, setExcelName] = useState('Новый файл');
    
    const [data, setData] = useState(null);
    
    var d = [];
    
    const [render, setRender] = useState(false);
    
    // useState для таблицы
    
    const [tableHead,setTableHead] = useState(null);
    const [tableBody,setTableBody] = useState(null);
    
    // useState для поля ввода
    
    const [textFilter, setTextFilter] = useState(null);
    
    // Получение даты из redux
    
    const selects = String(useSelector(state => state.periodReducer).dateBegin);
    const selects1 = String(useSelector(state => state.periodReducer).dateEnd);

    useEffect(()=>{
        setTableBody(null);
        setTableHead(null);
        fetchData();
    },[textFilter,selects,selects1]);

    // Список для названия столбцов

    const names = new Array('Должность',"Время начала","Время конца",'Комнаты');

    // Метод для получения данных за определённый промежуток времени

    const fetchData = () => {
        axios.post('http://technolog.bzf.asu/lineman/repots/filter/room',{ 'rep_start_time': selects, 'rep_stop_time': selects1 })
        // axios.get('http://localhost:8000/lineman/repots/filter/room').then(succs=>{console.log(succs);});
        // axios.post('http://localhost:8000/lineman/repots/filter/room',{ 'rep_start_time': selects, 'rep_stop_time': selects1 })
        .then(response=>parseResponse(response)
        .then(succs=>prepairTableBody(succs))
        .then(succs=>createTable(succs)));
    };

    const parseResponse = (data) => {
        return new Promise((resolve, reject) => {
            let dataFun = data.data;
            for (const e in dataFun){
                d.push(JSON.parse(dataFun[e].rep_string));
                fetchDataRoom(dataFun[e].rep_rooms).then(succs => {dataFun[e].rep_names = succs[0];dataFun[e].rep_mass = succs[1]});
            }
            setExcel(d);
            setTimeout(()=>{resolve(dataFun);},500);
        })
    }

    // Метод для создания таблицы

    const prepairTableBody = (some) =>{
        var newMass;
        return new Promise((resolve, reject) => {
            newMass = some.map((e)=>{
                try {
                    if(textFilter === null){
                        return(
                            <tr>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_name}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_start_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_stop_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><button style={{whiteSpace:'pre-line'}} className="btnn" id={e.id} onClick={()=>{setData(e);manageRender()}}>{e.rep_names}</button></td>
                            </tr>
                        )
                    }
                    if (textFilter.target.value === ''){
                        return(
                            <tr>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_name}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_start_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_stop_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><button style={{whiteSpace:'pre-line'}} className="btnn" id={e.id} onClick={()=>{setData(e);manageRender()}}>{e.rep_names}</button></td>
                            </tr>
                        )
                    }
                    if (e.rep_name.toLowerCase().replaceAll(' ','').includes(textFilter.target.value.toLowerCase().replaceAll(' ',''))){
                        return(
                            <tr>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_name}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_start_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_stop_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><button style={{whiteSpace:'pre-line'}} className="btnn" id={e.id} onClick={()=>{setData(e);manageRender()}}>{e.rep_names}</button></td>
                            </tr>
                        )
                    } else if (e.rep_names.toLowerCase().replaceAll(' ','').includes(textFilter.target.value.toLowerCase().replaceAll(' ',''))){
                        return(
                            <tr>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_name}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_start_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><p style={{display:'flex',justifyContent:'center'}}>{e.rep_stop_time.split(".")[0].replace("T","/").replace("Z","")}</p></td>
                                <td><button style={{whiteSpace:'pre-line'}} className="btnn" id={e.id} onClick={()=>{setData(e);manageRender()}}>{e.rep_names}</button></td>
                            </tr>
                        )
                    }
                    else{
                        return "";
                    }
                } catch (error) {
                    // console.log(error);
                }
            })
            resolve(newMass);
        })
    }

    const createTable = (data)=>{
        if (data.length === 0){
            setTableHead(()=>{
                return(
                    <td style={{color:'#000000'}}>Нет данных за этот период времени</td>
                )
            })
        }
        else if (data.every((value)=>value==='')) {
            setTableHead(()=>{
                return(
                    <td style={{color:'#000000'}}>Нет данных удовлетворяющих поиску</td>
                )
            })
        }
        else{
            setTimeout(()=>{
                setTableBody(null);
                setTableHead(null);
                setRender(true);
                setTableHead(()=>{
                    return(
                        <tr>
                            {
                                names.map((e)=>{
                                    return(
                                        <th style={{position:'sticky',top:'0', backgroundColor:'black'}}>{e}</th>
                                    )
                                })
                            }
                        </tr>
                    )
                });
                setTableBody(data);
            },500);
        }
    }

    // Метод для получения комнат

    const fetchDataRoom = (asd) => {
        var lsjdf = '';
        var aeseg = [];
        var ij = axios.post('http://technolog.bzf.asu/lineman/kys/room',{'room' : asd}).then((response)=>{
            // var ij = axios.post('http://localhost:8000/lineman/kys/room',{'room' : asd}).then((response)=>{
            for (let i = 0; i < response.data.length; i++) {
                lsjdf += response.data[i].room_r + '\n';
                aeseg.push(response.data[i].room_r);
            }
            return [lsjdf,aeseg];
        });
        return ij;
    }

    const renderExcel = () => {
        if(render){
            return(
                <>
                <p className="excelLabel">Название excel файла</p>
                <input type="text" className="excelInput" placeholder='Новый файл' onChange={(e)=>{setExcelName(e.target.value)}}/>
                <Test pres={excel} name1={excelName}/>
                </>
            )
        }else{
            return(
                <p></p>
            )
        }
    }

    return (
        <div className="tpm">
            <ReactModal isOpen={renderModal} className='myModel' onRequestClose={manageRender} ariaHideApp={false}>
                <button className="modalButton" onClick={()=>{manageRender()}}>Закрыть окно</button>
                <ModalClass data={data} />
            </ReactModal>
            <div className="upperContainer">
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
                    <button className="buttonDate"onClick={()=>{fetchData();}}>Обновить таблицу</button>
                </div>
                <div className="searchContainerMain">
                    {/* <div className="textSearch">
                        <p className="textDate">Поиск</p>
                    </div> */}
                    <div className="searchContainer">
                        <input className="searchStyle" placeholder="Поиск" type="text" name="search" onChange={(e)=>{setTextFilter(e)}}/>
                    </div>
                </div>
            </div>
            <div className='mainContainer'>
                <div className="filterContainer">
                    {renderExcel()}
                </div>
                <div className="tableContainer">
                    <div className="tableTable">
                        <table className="table">
                            <thead><tr><td style={{width:'1445px',display:'flex',alignItems:'center',justifyContent:'center',fontSize:'x-large'}}>Отчёты</td></tr></thead>
                            <tbody>
                                <table style={{display:'block',overflowY:'auto',height:'560px', width:'1465px'}}>
                                    <thead className="tableHead">{tableHead}</thead>
                                    <tbody className="tableBody">{tableBody}</tbody>
                                </table>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    ) 
}