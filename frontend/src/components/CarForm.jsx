import React, { useState } from 'react';
import { Box, Button, MenuItem, TextField, Typography, Alert, CircularProgress } from '@mui/material';
import axios from 'axios';

const tipos = [
  { value: 'carro', label: 'Carro' },
  { value: 'moto', label: 'Moto' },
  { value: 'caminhao', label: 'Caminhão' },
  { value: 'todos', label: 'Todos' },
];
const placas = [
  { value: 'aleatoria', label: 'Aleatória' },
  { value: 'mercosul', label: 'Mercosul (ABC1D23)' },
  { value: 'antiga', label: 'Antiga (ABC-1234)' },
];

export default function CarForm() {
  const [quantity, setQuantity] = useState(1);
  const [tipo, setTipo] = useState('carro');
  const [placa, setPlaca] = useState('aleatoria');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);
    try {
      const res = await axios.post('/api/veiculos/veiculos/generate/', {
        quantity: Number(quantity),
        tipo_veiculo: tipo,
        formato_placa: placa,
      });
      setResult(res.data);
    } catch (err) {
      setError(err.response?.data?.message || 'Erro ao gerar veículos');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mb: 4, p: 2, border: '1px solid #eee', borderRadius: 2 }}>
      <Typography variant="h6" gutterBottom>Gerar Veículos Fakes</Typography>
      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mb: 2 }}>
        <TextField
          label="Quantidade"
          type="number"
          value={quantity}
          onChange={e => setQuantity(e.target.value)}
          inputProps={{ min: 1, max: 100 }}
          required
        />
        <TextField
          select
          label="Tipo de Veículo"
          value={tipo}
          onChange={e => setTipo(e.target.value)}
        >
          {tipos.map(opt => <MenuItem key={opt.value} value={opt.value}>{opt.label}</MenuItem>)}
        </TextField>
        <TextField
          select
          label="Formato da Placa"
          value={placa}
          onChange={e => setPlaca(e.target.value)}
        >
          {placas.map(opt => <MenuItem key={opt.value} value={opt.value}>{opt.label}</MenuItem>)}
        </TextField>
        <Button type="submit" variant="contained" disabled={loading} sx={{ minWidth: 150 }}>
          {loading ? <CircularProgress size={24} /> : 'Gerar'}
        </Button>
      </Box>
      {result && (
        <Alert severity="success" sx={{ mb: 2 }}>
          {result.message}
        </Alert>
      )}
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>
      )}
      {result?.data && Array.isArray(result.data) && (
        <Box sx={{ maxHeight: 300, overflow: 'auto', mt: 2 }}>
          <pre style={{ fontSize: 13 }}>{JSON.stringify(result.data, null, 2)}</pre>
        </Box>
      )}
    </Box>
  );
} 