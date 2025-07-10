import React, { useEffect, useState } from 'react';
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, TextField, Button, CircularProgress, Alert } from '@mui/material';
import axios from 'axios';

export default function CarList() {
  const [veiculos, setVeiculos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [filtros, setFiltros] = useState({ marca: '', categoria: '', situacao: '' });

  const fetchVeiculos = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = {};
      if (filtros.marca) params.marca = filtros.marca;
      if (filtros.categoria) params.categoria = filtros.categoria;
      if (filtros.situacao) params.situacao = filtros.situacao;
      const res = await axios.get('/api/veiculos/veiculos/', { params });
      setVeiculos(res.data.results || res.data.data || []);
    } catch (err) {
      setError('Erro ao buscar veículos');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchVeiculos();
    // eslint-disable-next-line
  }, []);

  const handleFiltroChange = (e) => {
    setFiltros({ ...filtros, [e.target.name]: e.target.value });
  };

  const handleFiltrar = (e) => {
    e.preventDefault();
    fetchVeiculos();
  };

  return (
    <Box sx={{ mb: 4 }}>
      <Typography variant="h6" gutterBottom>Veículos Salvos no Banco</Typography>
      <Box component="form" onSubmit={handleFiltrar} sx={{ display: 'flex', gap: 2, mb: 2, flexWrap: 'wrap' }}>
        <TextField label="Marca" name="marca" value={filtros.marca} onChange={handleFiltroChange} />
        <TextField label="Categoria" name="categoria" value={filtros.categoria} onChange={handleFiltroChange} />
        <TextField label="Situação" name="situacao" value={filtros.situacao} onChange={handleFiltroChange} />
        <Button type="submit" variant="outlined">Filtrar</Button>
        <Button variant="text" onClick={() => { setFiltros({ marca: '', categoria: '', situacao: '' }); fetchVeiculos(); }}>Limpar</Button>
      </Box>
      {loading ? <CircularProgress /> : error ? <Alert severity="error">{error}</Alert> : (
        <TableContainer component={Paper} sx={{ maxHeight: 350 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell>Placa</TableCell>
                <TableCell>Marca</TableCell>
                <TableCell>Modelo</TableCell>
                <TableCell>Ano</TableCell>
                <TableCell>Cor</TableCell>
                <TableCell>Categoria</TableCell>
                <TableCell>Situação</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {veiculos.length === 0 ? (
                <TableRow><TableCell colSpan={7} align="center">Nenhum veículo encontrado</TableCell></TableRow>
              ) : veiculos.map((v) => (
                <TableRow key={v.id}>
                  <TableCell>{v.placa}</TableCell>
                  <TableCell>{v.marca}</TableCell>
                  <TableCell>{v.modelo}</TableCell>
                  <TableCell>{v.ano_fabricacao}</TableCell>
                  <TableCell>{v.cor}</TableCell>
                  <TableCell>{v.categoria}</TableCell>
                  <TableCell>{v.situacao}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
} 