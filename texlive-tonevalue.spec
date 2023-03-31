Name:		texlive-tonevalue
Version:	60058
Release:	2
Summary:	Tool for linguists and phoneticians to visualize tone value patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tonevalue
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tonevalue.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tonevalue.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a TikZ-based solution to typeset
visualisations of tone values. Currently, unt's model is
implemented. Support for more models is planned.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tonevalue
%doc %{_texmfdistdir}/doc/latex/tonevalue

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
