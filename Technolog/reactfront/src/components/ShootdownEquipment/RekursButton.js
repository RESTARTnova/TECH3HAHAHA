import React, {useState} from "react";


export default function RekursButton(props){

    const [click, setClick] = useState(false)
    const [element, setElement] = useState()

    function requrs(){
        setClick(true)
        setElement(()=>{
            // const element = ()=>{
                console.log('click='+click)
                if (!click){
                    setClick(true)
                    return <RekursButton value={Number(props.value)+1}/>
                }
                else {
                    setClick(false)
                    return null
                }
            })
    }


    return <div className='requrs'>
        <button onClick={()=>{requrs()}}>{props.value}</button>
        {element}

    </div>
}