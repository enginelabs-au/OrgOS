import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Papership from './pages/papership';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/papership" replace />} />
        <Route path="/papership" element={<Papership />} />
        <Route path="/cc-org-dash" element={<Navigate to="/papership" replace />} />
        <Route path="/EcoOS" element={<Navigate to="/papership" replace />} />
        <Route path="/ecoos" element={<Navigate to="/papership" replace />} />
        <Route path="/Dashboard_new" element={<Navigate to="/papership" replace />} />
        <Route path="/Dashboard" element={<Navigate to="/papership" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
