import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import HomePage from './components/pages/HomePage';
import PublisherPage from './components/pages/PublisherPage'; // Import PublisherPage component
import AdvertiserPage from './components/pages/AdvertiserPage';

function App() {
  return (
    <Router>
      <div style={{ display: 'flex' }}>
        <NavBar />
        <div style={{ padding: '20px' }}>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/inventory/publisher" element={<PublisherPage />} /> {/* Add route for PublisherPage */}
            <Route path="/demand/advertiser" element={<AdvertiserPage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
