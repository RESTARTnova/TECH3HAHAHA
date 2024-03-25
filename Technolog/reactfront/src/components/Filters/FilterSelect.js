import React, {useState, useEffect} from "react";

export default function FilterSelect(props){

    const [flag, setFlag] = useState(true)
    const [checkmark, setChekmark] = useState('')
    const [classVis, setClassVis] = useState('no-show')
    const [options, setOptions] = useState(()=>{
        let arr={}
        for (let i=0; i<(props.arr.length); i++)
        {
            arr[props.arr[i]] = ['non-checked', <p>&#9723;</p>]
        }
        
        // console.log(arr)
        return arr
    })
    console.log('props.isVisible = '+ props.arr)

    useEffect(()=>{
       
        if(props.isVisible){
            setClassVis('filter-class')
        }
        else {
            
            setClassVis('no-show')
        }
    }, [props.isVisible, flag]
    )
    function handleDoubleClick(e){
        
        setOptions(()=>{
            
            let my_obj = options
            Object.keys(my_obj).map((t)=>{console.log('from handleDoubleClick'+t)})
            console.log('my_obj[e.target.value] = '+my_obj[e.target.value])
            if(my_obj[e.target.value][0]=='checked-option')
            {
                my_obj[e.target.value][0] = 'non-checked'
                my_obj[e.target.value][1] = <p>&#9723;</p>
            }
            else{
                my_obj[e.target.value][0] = 'checked-option'
                my_obj[e.target.value][1] = <p>&#128505;</p>
                // setChekmark('&#9723;')
            }
                

            return my_obj
        })
        
        setFlag(!flag)
        console.log(e.target.className)
        console.log(e.target.value)
        
    }

    function handleClick(){
        props.handlerVis()
    }
    let i=0
    return (<div className={classVis}  >
            <select multiple>
                {Object.keys(props.arr).map((e)=>{
                    i++
                    return (<option  onClick={handleDoubleClick} className={options[props.arr[e]][0]} value={props.arr[e]}>{options[props.arr[e]][1]}{props.arr[e]}</option>)
                    // return (<option onDoubleClick={(e)=>{handleDoubleClick(e, i)}} className={optionClass} value={props.arr[e]}><input type="chekbox"/></option>)
                })}
            </select>
            
            <button onClick={()=>{
                handleClick()
                setClassVis('no-show')}}>Применить</button>
        </div>)

}