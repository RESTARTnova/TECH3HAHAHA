
import './App.css';
import axios from 'axios'
import React, {useState, useEffect} from "react"

export default function App() {
  const[post, setPost] = useState(null)
  useEffect(() => {
    axios.get('http://localhost:8000/factory/test_resp/').then((response)=>{
      setPost(response.data)
    })
  },[setPost])
  console.log(post)

  if(!post) return null

  return (
    <div>
      <p>{post.name}</p>
    </div>
  )

}

// function App() {

//   const DataLoading = loadingData(testData)

//   const [appState, setAppState] = useState(
//     {
//       loading: false,
//       test_pers: null,
//     }

//   )

//   useEffect (() => {
//     setAppState({loading: true})
//     console.log(" чтото ")
//     const apiURL = 'http://localhost:8000/factory/test_resp/'
//     axios.get(apiURL).then((resp) =>{
//       console.log(resp)
//       console.log(resp.data)
//       const allMachines = resp.data
//       // setAppState(allMachines)
//       setAppState({
//         loading: false,
//         test_pers: allMachines,
//       })

//     })
//   },[setAppState])
//   console.log(appState)
  

//   return (
//     <div className="App">
//       <DataLoading isLoading={appState.loading} test_pers={appState.test_pers} />
      
//     </div>
//   );
// }

// export default App;

// import React from 'react';
// import { trackPromise, usePromiseTracker } from 'react-promise-tracker';

// const area = 'persons';
// const apiUrl = 'http://localhost:8000/factory/test_resp/';

// const App = () => {
//     const { promiseInProgress } = usePromiseTracker({ area });
//     const [ persons, setPersons ] = useState(null);

//     useEffect(() => {
//       trackPromise(axios.get(apiUrl), area).then(({ data }) => {
//         setPersons(data);
//       });
//     }, [setPersons]);
//     console.log(setPersons)
//     return (
//       <div className="app">
//           {promiseInProgress
//             ? <div>Подождите, данные загружаются!</div>
//             : <div >{persons.name}</div> }
//       </div>
//     );
//   }

//   export default App;
