import React, { useState } from 'react';
import { Container, AppBar, Toolbar, Typography, Tabs, Tab, Box } from '@mui/material';
import DirectionsCarIcon from '@mui/icons-material/DirectionsCar';
import PeopleIcon from '@mui/icons-material/People';
import CarForm from './components/CarForm';
import CarList from './components/CarList';
import CarStats from './components/CarStats';
import CarActions from './components/CarActions';
import PersonForm from './components/PersonForm';
import PersonProfile from './components/PersonProfile';

function TabPanel(props) {
  const { children, value, index, ...other } = props;
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`tabpanel-${index}`}
      aria-labelledby={`tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

export default function App() {
  const [tab, setTab] = useState(0);

  const handleChange = (event, newValue) => {
    setTab(newValue);
  };

  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <DirectionsCarIcon sx={{ mr: 1 }} />
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Plataforma de Testes de Dados Fakes
          </Typography>
        </Toolbar>
        <Tabs value={tab} onChange={handleChange} centered>
          <Tab icon={<DirectionsCarIcon />} label="Veículos" />
          <Tab icon={<PeopleIcon />} label="Pessoas" />
        </Tabs>
      </AppBar>
      <Container maxWidth="md" sx={{ mt: 4 }}>
        <TabPanel value={tab} index={0}>
          <CarActions />
          <CarForm />
          <CarList />
          <CarStats />
        </TabPanel>
        <TabPanel value={tab} index={1}>
          <PersonForm />
          <PersonProfile />
        </TabPanel>
      </Container>
    </>
  );
}
