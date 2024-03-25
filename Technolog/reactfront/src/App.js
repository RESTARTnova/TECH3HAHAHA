
import './App.scss';
import {BrowserRouter, Routes, Route, Link, NavLink} from 'react-router-dom'
import {connect} from 'react-redux'
// import Main from './components/main/Main'
import Tpm from './components/tpm/Tpm'
import ShootdownEquipment from './components/ShootdownEquipment/ShootdownEquipment'
import Testing from './components/Testing/Testing'
// Testing


function App() {
  console.log('App rendered')
  return (
    <BrowserRouter>
      <div>
        <div className='header'>
          <div className="logo"></div>
                <ul>      
                    <li><NavLink to="/shootdown_f">Главная</NavLink></li> 
                    <li><NavLink to="/shootdown_f">База оборудования</NavLink></li> 
                    <li><NavLink to="/shootdown_f">Технолог</NavLink></li> 
                    {/* <li><button className='btn_main_menu' onClick={}></button></li> */}
                    <li><NavLink to="/shootdown_f">Простои</NavLink></li> 
                    <li><NavLink to="/tpm_f">TPM</NavLink></li> 
                    <li><NavLink to="/testing_f">TEST</NavLink></li>               
                </ul>
          </div>
          {/*trsjhytjs*/}
          <div className='content'>
              <div className='sidebar'>
                <p>Some info</p>
              </div>
              <div className='routes'>
              <Routes>
                <Route path="tpm_f" element={<Tpm/>} /> 
                <Route path="shootdown_f" element={<ShootdownEquipment/>} />
                <Route path="testing_f" element={<Testing/>} />
              </Routes>
              </div>
          </div>
          
          
        
          <div className="footer">
              <p>МЕЧЕЛ</p>
        </div>
      </div>
    </BrowserRouter>
    
    
  )

}
export default connect()(App)