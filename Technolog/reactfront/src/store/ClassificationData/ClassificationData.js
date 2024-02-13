import { createSlice } from "@reduxjs/toolkit";



export const classDataSlice = createSlice({
    name:'classData',
    initialState:{
        flag_classification:true,
        id:0,
        class_shutdown:'',
        type_shutdown:0,
        factor_shutdown:0,
    },
    reducers:{
        putFlag: (state,action) =>{
            state.flag_classification = action.payload.flag
        },
        put_id:(state, action) =>{
            state.id = action.payload.id
        },
        putClassStdn:(state, action) => {
            state.class_shutdown = action.payload.value
            state.type_shutdown = 0
            state.factor_shutdown = 0
        },
        putTypeStdn:(state, action) => {
            state.type_shutdown = action.payload.value
            state.factor_shutdown = 0
        },
        putFactStdn:(state, action) => {
         
            state.factor_shutdown= action.payload.value
        },
    }

})

export const {putClassStdn, putFactStdn, putTypeStdn, put_id, putFlag} = classDataSlice.actions

export default classDataSlice.reducer