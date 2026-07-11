%global tl_name tonevalue
%global tl_revision 60058

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Tool for linguists and phoneticians to visualize tone value patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tonevalue
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tonevalue.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tonevalue.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a TikZ-based solution to typeset visualisations of
tone values. Currently, unt's model is implemented. Support for more
models is planned.

