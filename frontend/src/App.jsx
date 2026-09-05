import React from "react";
import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Dashboard from "./components/Dashboard";
import ParameterDetail from "./components/ParameterDetail";
import EntryForm from "./components/EntryForm";
import EntryList from "./components/EntryList";
import SettingsPage from "./components/SettingsPage";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Dashboard />} />
        <Route path="/parameter/:code" element={<ParameterDetail />} />
        <Route path="/neu" element={<EntryForm />} />
        <Route path="/eintraege" element={<EntryList />} />
        <Route path="/eintraege/:id/bearbeiten" element={<EntryForm />} />
        <Route path="/einstellungen" element={<SettingsPage />} />
      </Route>
    </Routes>
  );
}
