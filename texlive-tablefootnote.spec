# revision 32804
# category Package
# catalog-ctan /macros/latex/contrib/tablefootnote
# catalog-date 2014-01-21 19:24:06 +0100
# catalog-license lppl1.3
# catalog-version 1.1b
Name:		texlive-tablefootnote
Version:	1.1b
Release:	5
Summary:	Permit footnotes in tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablefootnote
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the command \tablefootnote to be used in a
table or sidewaystable environment, where \footnote will not
work (and when using \footnotemark and \footnotetext, and
adjusting the counter as necessary, is too much work).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tablefootnote/tablefootnote.sty
%doc %{_texmfdistdir}/doc/latex/tablefootnote/README
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote-example.pdf
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote-example.tex
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.drv
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.dtx
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
