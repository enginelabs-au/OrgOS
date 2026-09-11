import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import CcOrgDash from './pages/cc-org-dash';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/cc-org-dash" replace />} />
        <Route path="/papership" element={<Navigate to="/cc-org-dash" replace />} />
        <Route path="/EcoOS" element={<Navigate to="/cc-org-dash" replace />} />
        <Route path="/ecoos" element={<Navigate to="/cc-org-dash" replace />} />
        <Route path="/cc-org-dash" element={<CcOrgDash />} />
        <Route path="/Dashboard_new" element={<Navigate to="/cc-org-dash" replace />} />
        <Route path="/Dashboard" element={<Navigate to="/cc-org-dash" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
