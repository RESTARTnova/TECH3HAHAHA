import axios from 'axios'
import React, {useState, useEffect} from "react"


export default function ShootdownClassification() 
{
    const[post, setPost] = useState(null)

    useEffect(() => {
        axios.get('http://technolog.bzf.asu/shutdown/get_shutdowns/').then((response)=>{
        // axios.get('http://localhost:8000/shutdown/get_shutdowns/').then((response)=>{
          setPost(response.data)
        })
      },[])
}