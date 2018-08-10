{{/*
Create a default fully qualified app name.
*/}}
{{- define "clara.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name | trunc 63 | trimSuffix "-" -}}
{{-- end }}