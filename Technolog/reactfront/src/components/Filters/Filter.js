import filter from './filter.png'
import clear_filter from './clear_filter.png'
import './Filter.scss'
import FilterSelect from './FilterSelect'
import React, {useState}  from 'react'


export default function Filter(props){

    const [isVisible, setVisible] =useState(false)

    function handleFilter(){
        
        console.log('нажали фильтр')
        setVisible(!isVisible)
    }

    function handleClear(){
        console.log('нажали очистку фильтра')
    }

    return <div className="Filter">
        
        <div className='filter-block'>
            <div className='tab-header'><p>{props.name}</p></div>
            <div>
                <button onClick={handleFilter} ><img className='filter-icon' src={filter}/></button>
                
                <button onClick={handleClear}><img className='filter-icon' src={clear_filter}/></button>

            </div>
            
        </div>
        <FilterSelect arr={props.arr} isVisible={isVisible} handlerVis={handleFilter}/>
        
    </div>
        // (<select >
        //     {Object.keys(props.arr).map((e)=>{/home/ubunty_server_20_04/Technolog/Technolog/reactfront/src/icons/clear_filter.png
        //         return <option>{e}</option>
        //     })}
        // </select>)

}