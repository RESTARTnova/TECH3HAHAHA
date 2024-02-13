import {configureStore} from '@reduxjs/toolkit'
import getDateBeginReducer from '../store/dateGetter/dateGetter'
import classDataReducer from '../store/ClassificationData/ClassificationData'

export default configureStore({
    reducer:{
        periodReducer: getDateBeginReducer ,
        classificationDataReducer: classDataReducer,
    },
})