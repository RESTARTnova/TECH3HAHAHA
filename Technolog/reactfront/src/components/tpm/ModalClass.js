import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './ModalClassStyle.scss'

export default function ModalClass(data) {

    var mass = data.data;

    var info2 = [];

    const [table, setTable] = useState('Загрузка');

    const [log, setLog] = useState('Загрузка');

    // console.log(mass);

    useEffect(()=>{
        test();
    },[]);

    var dataMass = [];

    var anotherMass = [];

    const getLogs = () => {
        axios.post('http://localhost:8000/lineman/log',{"ids":mass.rep_logs})
        .then(succs=>{
            createLogs(succs.data).then(succs1=>{setLog(succs1)});
        })
    }

    const createLogs = (data) => {
        var massw;
        return new Promise((resolve, reject) => {
            massw = data.map((e)=>{
                return(
                    <tr style={{backgroundColor:'black'}}>
                        <td>{e.timel}</td>
                        <td>{e.logl}</td>
                    </tr>
                )
            });
            setTimeout(()=>{resolve(massw)},2000);
        })
    }

    const fetchData = ()=>{
        getLogs();
        var kli = [];
        var ij = axios.post('http://technolog.bzf.asu/lineman/kys/room',{'room' : mass.rep_rooms}).then((response)=>{
        // var ij = axios.post('http://localhost:8000/lineman/kys/room',{'room' : mass.rep_rooms}).then((response)=>{
            for (let i = 0; i < response.data.length; i++) {
                kli.push(response.data[i]);
            }
            return kli;
        })
        return ij;
    }

    const parseData = (rooms)=>{
        var kli = [];
        var result = [];
        var ij = 1;
        for (let i = 0; i < rooms.length; i++) {
            ij = 1;
            ij = axios.post('http://technolog.bzf.asu/lineman/kys/action',{'action' : rooms[i].actions_r}).then((response)=>{
            // ij = axios.post('http://localhost:8000/lineman/kys/action',{'action' : rooms[i].actions_r}).then((response)=>{
                kli = [];
                for (let i = 0; i < response.data.length; i++) {
                    kli.push(response.data[i]);
                }
                return kli;
            })
            result.push(ij);
        }
        info2 = result;
    }

    const createData = (needMass) => {
        dataMass = [];
        for(const l of needMass){
            dataMass.push(l);
        }
    }

    const test = () => {
        fetchData().then(succs => parseData(succs)).then(succs=>{goingInCycle().then(succs=>setBody(succs).then(succs=>{setTable(succs)}))});
    }

    const goingInCycle = () => {
        anotherMass = [];
        return new Promise((resolve, reject) => {
            Promise.all(info2).then(succs=>{
                succs.map((e)=>{
                    createData(e);
                    anotherMass.push(dataMass);
                });
            });
            setTimeout(()=>{resolve(anotherMass)},1000);
        })
    }

    const setBody = (data) => {
        return new Promise((resolve, reject) => {
            var eh = data.map((e,i)=>{
                return(
                    <td style={{backgroundColor:'black',color:'white'}}>
                            <tr >{mass.rep_mass[i]}</tr>
                            <tr>{createTd(e)}
                            </tr>
                        </td>
                    )
                })
            setTimeout(()=>{resolve(eh)},1000);
        })
    }

    const createTd = (el) => {
        if (el.length === 0){
            return(
                <td style={{maxWidth:'350px',color:'black'}}>Нет замечаний</td>
            )
        }
        return el.map((q,i)=>{
            return(
                <tr>
                    <td style={{color:'black'}}>{q.name_r}</td>
                    <td className='row'>{q.remark_r === "" ? 'Нет ошибок' : q.remark_r}</td>
                </tr>
            )
        })
    }

    return(
        <div style={{display:'flex',flexDirection:'row'}}>
            <div>
                <p style={{fontSize:"x-large"}}>Комнаты</p>
                <table>
                    {table}
                </table>
            </div>
            <div>
                <p style={{fontSize:"x-large"}}>История</p>
                {log}
            </div>
        </div>
    )
}
