import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'

function Home() {
  return <></>
}

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  )
}
