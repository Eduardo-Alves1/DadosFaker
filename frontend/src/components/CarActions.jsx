import React, { useState } from 'react';
import { Box, Button, Alert, CircularProgress, Stack } from '@mui/material';
import axios from 'axios';

export default function CarActions() {
  const [loading, setLoading] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [veiculoPronto, setVeiculoPronto] = useState(null);

  const handleSave = async () => {
    setLoading('save'); setResult(null); setError(null);
    try {
      // Exemplo: salva 1 carro com placa aleatória
      const res = await axios.post('/api/veiculos/veiculos/save/', {
        quantity: 1,
        tipo_veiculo: 'carro',
        formato_placa: 'aleatoria',
      });
      setResult(res.data.message || 'Veículo salvo!');
    } catch (err) {
      setError(err.response?.data?.message || 'Erro ao salvar veículo');
    } finally {
      setLoading('');
    }
  };

  const handleLimpar = async () => {
    setLoading('limpar'); setResult(null); setError(null);
    try {
      const res = await axios.delete('/api/veiculos/veiculos/limpar/');
      setResult(res.data.message || 'Banco limpo!');
    } catch (err) {
      setError(err.response?.data?.message || 'Erro ao limpar banco');
    } finally {
      setLoading('');
    }
  };

  const handlePronto = async () => {
    setLoading('pronto'); setError(null); setResult(null);
    try {
      const res = await axios.get('/api/veiculos/veiculos/pronto/');
      setVeiculoPronto(res.data.data || res.data);
    } catch (err) {
      setError('Erro ao gerar veículo pronto');
    } finally {
      setLoading('');
    }
  };

  return (
    <Box sx={{ mb: 3 }}>
      <Stack direction="row" spacing={2}>
        <Button variant="contained" color="success" onClick={handleSave} disabled={loading==='save'}>
          {loading==='save' ? <CircularProgress size={20} /> : 'Salvar Veículo no Banco'}
        </Button>
        <Button variant="outlined" color="error" onClick={handleLimpar} disabled={loading==='limpar'}>
          {loading==='limpar' ? <CircularProgress size={20} /> : 'Limpar Banco'}
        </Button>
        <Button variant="outlined" onClick={handlePronto} disabled={loading==='pronto'}>
          {loading==='pronto' ? <CircularProgress size={20} /> : 'Gerar Veículo Pronto'}
        </Button>
      </Stack>
      {result && <Alert severity="success" sx={{ mt: 2 }}>{result}</Alert>}
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
      {veiculoPronto && (
        <Alert severity="info" sx={{ mt: 2, maxHeight: 300, overflow: 'auto' }}>
          <pre style={{ fontSize: 13 }}>{JSON.stringify(veiculoPronto, null, 2)}</pre>
        </Alert>
      )}
    </Box>
  );
} 