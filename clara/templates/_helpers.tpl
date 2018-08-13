{{/* vim: set filetype=mustache: */}}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
