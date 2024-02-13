import { createSlice } from "@reduxjs/toolkit"



function getMonth(x){
    x+=1
    if (x<10){
        return '0'+x
    }
    else {
        return x.toString()
    }
}
function getDay(x){
    
    if (x<10){
        return '0'+x
    }
    else {
        return x.toString()
    }
}
const nowDate =new Date()
const year = nowDate.getFullYear()
const month = getMonth(nowDate.getMonth())

const day = getDay(nowDate.getDate())
export const getDateBeginSlice = createSlice({
    name: 'getDateBegin',
    initialState: {
        dateBegin: year.toString()+'-' + month + '-' + '01',
        dateEnd: year.toString()+'-' + month +'-' + day,
        value: '254'
    },
    reducers: {

        testik: (state, action) => {
            
            // state.dateBegin = action.payload.begin
            state.dateEnd= action.payload.end
          },
        putBegin: (state, action) => {
            state.dateBegin = action.payload.begin
        },
        putEnd: (state, action) => {
            state.dateEnd = action.payload.end
        },
    }
})

export const {testik, putBegin, putEnd} = getDateBeginSlice.actions

export default getDateBeginSlice.reducer